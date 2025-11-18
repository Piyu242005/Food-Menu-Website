"""
Main routes - Homepage and menu display
"""
from flask import render_template, request, jsonify
from app.main import bp
from app.models import MenuItem, Category
from app import db

@bp.route('/')
def index():
    """Homepage with featured items"""
    categories = Category.query.order_by(Category.display_order).all()
    featured_items = MenuItem.query.filter_by(is_available=True).limit(6).all()
    return render_template('index.html', categories=categories, featured_items=featured_items)

@bp.route('/menu')
def menu():
    """Full menu page with filtering"""
    category_id = request.args.get('category', type=int)
    search_query = request.args.get('search', '').strip()
    dietary = request.args.get('dietary', '').strip()
    
    # Start with base query
    query = MenuItem.query.filter_by(is_available=True)
    
    # Apply filters
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    if search_query:
        query = query.filter(MenuItem.name.contains(search_query) | 
                           MenuItem.description.contains(search_query))
    
    if dietary:
        query = query.filter(MenuItem.dietary_tags.contains(dietary))
    
    # Get results
    menu_items = query.all()
    categories = Category.query.order_by(Category.display_order).all()
    
    return render_template('menu/menu.html', 
                         menu_items=menu_items, 
                         categories=categories,
                         selected_category=category_id,
                         search_query=search_query,
                         dietary_filter=dietary)

@bp.route('/menu/item/<int:item_id>')
def item_detail(item_id):
    """Individual menu item detail page"""
    item = MenuItem.query.get_or_404(item_id)
    related_items = MenuItem.query.filter_by(
        category_id=item.category_id,
        is_available=True
    ).filter(MenuItem.id != item_id).limit(4).all()
    
    return render_template('menu/item_detail.html', item=item, related_items=related_items)

@bp.route('/api/menu/search')
def api_search():
    """API endpoint for live search"""
    query = request.args.get('q', '').strip()
    
    if not query or len(query) < 2:
        return jsonify([])
    
    items = MenuItem.query.filter(
        MenuItem.is_available == True,
        (MenuItem.name.contains(query) | MenuItem.description.contains(query))
    ).limit(10).all()
    
    results = [{
        'id': item.id,
        'name': item.name,
        'price': item.price,
        'category': item.category.name,
        'image_url': item.image_url
    } for item in items]
    
    return jsonify(results)
