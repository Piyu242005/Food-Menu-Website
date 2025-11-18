"""
Admin routes - Dashboard and management
"""
import os
from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from functools import wraps
from app.admin import bp
from app.forms import MenuItemForm, CategoryForm
from app.models import MenuItem, Category, Order, OrderItem, User
from app import db

def admin_required(f):
    """Decorator to require admin role"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('You need admin privileges to access this page', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@login_required
@admin_required
def dashboard():
    """Admin dashboard"""
    total_orders = Order.query.count()
    pending_orders = Order.query.filter_by(status='pending').count()
    total_items = MenuItem.query.count()
    total_users = User.query.filter_by(role='customer').count()
    
    recent_orders = Order.query.order_by(Order.order_date.desc()).limit(10).all()
    
    return render_template('admin/dashboard.html',
                         total_orders=total_orders,
                         pending_orders=pending_orders,
                         total_items=total_items,
                         total_users=total_users,
                         recent_orders=recent_orders)

@bp.route('/menu-items')
@login_required
@admin_required
def menu_items():
    """Manage menu items"""
    items = MenuItem.query.all()
    return render_template('admin/menu_items.html', items=items)

@bp.route('/menu-items/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_menu_item():
    """Add new menu item"""
    form = MenuItemForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by(Category.name).all()]
    
    if form.validate_on_submit():
        item = MenuItem(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            category_id=form.category_id.data,
            dietary_tags=form.dietary_tags.data,
            preparation_time=form.preparation_time.data or 15,
            is_available=form.is_available.data
        )
        
        # Handle image upload
        if form.image.data:
            file = form.image.data
            filename = secure_filename(file.filename)
            # Add unique identifier to filename
            import uuid
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'menu_items', unique_filename)
            file.save(filepath)
            item.image_url = f"/static/uploads/menu_items/{unique_filename}"
        
        db.session.add(item)
        db.session.commit()
        
        flash(f'Menu item "{item.name}" added successfully!', 'success')
        return redirect(url_for('admin.menu_items'))
    
    return render_template('admin/menu_item_form.html', form=form, title='Add Menu Item')

@bp.route('/menu-items/edit/<int:item_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_menu_item(item_id):
    """Edit menu item"""
    item = MenuItem.query.get_or_404(item_id)
    form = MenuItemForm(obj=item)
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by(Category.name).all()]
    
    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        item.price = form.price.data
        item.category_id = form.category_id.data
        item.dietary_tags = form.dietary_tags.data
        item.preparation_time = form.preparation_time.data or 15
        item.is_available = form.is_available.data
        
        # Handle image upload
        if form.image.data:
            file = form.image.data
            filename = secure_filename(file.filename)
            import uuid
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'menu_items', unique_filename)
            file.save(filepath)
            
            # Delete old image if exists
            if item.image_url:
                old_filepath = os.path.join(current_app.root_path, item.image_url.lstrip('/'))
                if os.path.exists(old_filepath):
                    os.remove(old_filepath)
            
            item.image_url = f"/static/uploads/menu_items/{unique_filename}"
        
        db.session.commit()
        flash(f'Menu item "{item.name}" updated successfully!', 'success')
        return redirect(url_for('admin.menu_items'))
    
    return render_template('admin/menu_item_form.html', form=form, title='Edit Menu Item', item=item)

@bp.route('/menu-items/delete/<int:item_id>', methods=['POST'])
@login_required
@admin_required
def delete_menu_item(item_id):
    """Delete menu item"""
    item = MenuItem.query.get_or_404(item_id)
    
    # Delete image if exists
    if item.image_url:
        filepath = os.path.join(current_app.root_path, item.image_url.lstrip('/'))
        if os.path.exists(filepath):
            os.remove(filepath)
    
    db.session.delete(item)
    db.session.commit()
    
    flash(f'Menu item "{item.name}" deleted successfully!', 'success')
    return redirect(url_for('admin.menu_items'))

@bp.route('/categories')
@login_required
@admin_required
def categories():
    """Manage categories"""
    cats = Category.query.order_by(Category.display_order).all()
    return render_template('admin/categories.html', categories=cats)

@bp.route('/categories/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_category():
    """Add new category"""
    form = CategoryForm()
    
    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            description=form.description.data,
            display_order=form.display_order.data or 0
        )
        
        db.session.add(category)
        db.session.commit()
        
        flash(f'Category "{category.name}" added successfully!', 'success')
        return redirect(url_for('admin.categories'))
    
    return render_template('admin/category_form.html', form=form, title='Add Category')

@bp.route('/categories/edit/<int:category_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_category(category_id):
    """Edit category"""
    category = Category.query.get_or_404(category_id)
    form = CategoryForm(obj=category)
    
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        category.display_order = form.display_order.data or 0
        
        db.session.commit()
        flash(f'Category "{category.name}" updated successfully!', 'success')
        return redirect(url_for('admin.categories'))
    
    return render_template('admin/category_form.html', form=form, title='Edit Category', category=category)

@bp.route('/orders')
@login_required
@admin_required
def orders():
    """Manage orders"""
    status_filter = request.args.get('status', '')
    
    query = Order.query
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    orders_list = query.order_by(Order.order_date.desc()).all()
    
    return render_template('admin/orders.html', orders=orders_list, status_filter=status_filter)

@bp.route('/orders/<int:order_id>')
@login_required
@admin_required
def order_detail(order_id):
    """View order details"""
    order = Order.query.get_or_404(order_id)
    return render_template('admin/order_detail.html', order=order)

@bp.route('/orders/<int:order_id>/update-status', methods=['POST'])
@login_required
@admin_required
def update_order_status(order_id):
    """Update order status"""
    order = Order.query.get_or_404(order_id)
    new_status = request.form.get('status')
    
    if new_status in ['pending', 'confirmed', 'preparing', 'ready', 'delivered', 'cancelled']:
        order.status = new_status
        db.session.commit()
        flash(f'Order #{order.id} status updated to {new_status}', 'success')
    else:
        flash('Invalid status', 'danger')
    
    return redirect(url_for('admin.order_detail', order_id=order_id))
