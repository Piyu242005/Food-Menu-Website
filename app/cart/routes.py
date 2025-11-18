"""
Cart and checkout routes
"""
from flask import render_template, redirect, url_for, flash, session, request, jsonify
from flask_login import current_user, login_required
from app.cart import bp
from app.forms import CheckoutForm
from app.models import MenuItem, Order, OrderItem
from app import db

def get_cart():
    """Get cart from session"""
    return session.get('cart', {})

def save_cart(cart):
    """Save cart to session"""
    session['cart'] = cart
    session.modified = True

def calculate_cart_total(cart):
    """Calculate total price of items in cart"""
    total = 0
    for item_id, item_data in cart.items():
        item = MenuItem.query.get(int(item_id))
        if item:
            total += item.price * item_data['quantity']
    return round(total, 2)

@bp.route('/')
def view_cart():
    """View shopping cart"""
    cart = get_cart()
    cart_items = []
    total = 0
    
    for item_id, item_data in cart.items():
        item = MenuItem.query.get(int(item_id))
        if item:
            subtotal = item.price * item_data['quantity']
            cart_items.append({
                'item': item,
                'quantity': item_data['quantity'],
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('cart/cart.html', cart_items=cart_items, total=round(total, 2))

@bp.route('/add/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    """Add item to cart"""
    item = MenuItem.query.get_or_404(item_id)
    
    if not item.is_available:
        return jsonify({'success': False, 'message': 'Item is not available'}), 400
    
    cart = get_cart()
    item_id_str = str(item_id)
    
    if item_id_str in cart:
        cart[item_id_str]['quantity'] += 1
    else:
        cart[item_id_str] = {
            'quantity': 1,
            'name': item.name,
            'price': item.price
        }
    
    save_cart(cart)
    
    # Calculate cart totals
    cart_count = sum(item['quantity'] for item in cart.values())
    cart_total = calculate_cart_total(cart)
    
    return jsonify({
        'success': True,
        'message': f'{item.name} added to cart',
        'cart_count': cart_count,
        'cart_total': cart_total
    })

@bp.route('/update/<int:item_id>', methods=['POST'])
def update_cart(item_id):
    """Update item quantity in cart"""
    data = request.get_json()
    quantity = data.get('quantity', 1)
    
    if quantity < 0:
        return jsonify({'success': False, 'message': 'Invalid quantity'}), 400
    
    cart = get_cart()
    item_id_str = str(item_id)
    
    if quantity == 0:
        if item_id_str in cart:
            del cart[item_id_str]
    else:
        if item_id_str in cart:
            cart[item_id_str]['quantity'] = quantity
    
    save_cart(cart)
    
    cart_count = sum(item['quantity'] for item in cart.values())
    cart_total = calculate_cart_total(cart)
    
    return jsonify({
        'success': True,
        'cart_count': cart_count,
        'cart_total': cart_total
    })

@bp.route('/remove/<int:item_id>', methods=['POST'])
def remove_from_cart(item_id):
    """Remove item from cart"""
    cart = get_cart()
    item_id_str = str(item_id)
    
    if item_id_str in cart:
        item_name = cart[item_id_str]['name']
        del cart[item_id_str]
        save_cart(cart)
        
        cart_count = sum(item['quantity'] for item in cart.values())
        cart_total = calculate_cart_total(cart)
        
        return jsonify({
            'success': True,
            'message': f'{item_name} removed from cart',
            'cart_count': cart_count,
            'cart_total': cart_total
        })
    
    return jsonify({'success': False, 'message': 'Item not in cart'}), 404

@bp.route('/clear', methods=['POST'])
def clear_cart():
    """Clear all items from cart"""
    session['cart'] = {}
    session.modified = True
    return jsonify({'success': True, 'message': 'Cart cleared'})

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Checkout page"""
    cart = get_cart()
    
    if not cart:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('main.menu'))
    
    form = CheckoutForm()
    
    # Pre-fill form if user is logged in
    if current_user.is_authenticated and request.method == 'GET':
        form.customer_name.data = current_user.username
        form.customer_email.data = current_user.email
        form.phone_number.data = current_user.phone_number or ''
        form.delivery_address.data = current_user.address or ''
    
    if form.validate_on_submit():
        # Calculate total
        total = calculate_cart_total(cart)
        
        # Create order
        order = Order(
            user_id=current_user.id if current_user.is_authenticated else None,
            customer_name=form.customer_name.data,
            customer_email=form.customer_email.data,
            phone_number=form.phone_number.data,
            delivery_address=form.delivery_address.data,
            special_instructions=form.special_instructions.data,
            payment_method=form.payment_method.data,
            total_amount=total,
            status='pending'
        )
        
        db.session.add(order)
        db.session.flush()  # Get order ID
        
        # Create order items
        for item_id, item_data in cart.items():
            item = MenuItem.query.get(int(item_id))
            if item:
                order_item = OrderItem(
                    order_id=order.id,
                    menu_item_id=item.id,
                    quantity=item_data['quantity'],
                    price_at_purchase=item.price
                )
                db.session.add(order_item)
        
        db.session.commit()
        
        # Clear cart
        session['cart'] = {}
        session.modified = True
        
        flash(f'Order #{order.id} placed successfully! We will contact you soon.', 'success')
        return redirect(url_for('cart.order_confirmation', order_id=order.id))
    
    # Calculate cart items for display
    cart_items = []
    total = 0
    
    for item_id, item_data in cart.items():
        item = MenuItem.query.get(int(item_id))
        if item:
            subtotal = item.price * item_data['quantity']
            cart_items.append({
                'item': item,
                'quantity': item_data['quantity'],
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('cart/checkout.html', form=form, cart_items=cart_items, total=round(total, 2))

@bp.route('/order/<int:order_id>')
def order_confirmation(order_id):
    """Order confirmation page"""
    order = Order.query.get_or_404(order_id)
    
    # Check if user has access to this order
    if current_user.is_authenticated:
        if order.user_id != current_user.id and current_user.role != 'admin':
            flash('You do not have permission to view this order', 'danger')
            return redirect(url_for('main.index'))
    
    return render_template('cart/order_confirmation.html', order=order)

@bp.route('/cart-count')
def cart_count():
    """API endpoint to get cart count"""
    cart = get_cart()
    count = sum(item['quantity'] for item in cart.values())
    total = calculate_cart_total(cart)
    return jsonify({'count': count, 'total': total})
