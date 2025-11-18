"""
Food Menu Website - Main Entry Point
Run this file to start the Flask development server
"""
from app import create_app, db
from app.models import User, Category, MenuItem, Order, OrderItem

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Make database models available in Flask shell"""
    return {
        'db': db,
        'User': User,
        'Category': Category,
        'MenuItem': MenuItem,
        'Order': Order,
        'OrderItem': OrderItem
    }

@app.cli.command()
def create_admin():
    """Create an admin user"""
    from werkzeug.security import generate_password_hash
    
    admin = User(
        username='admin',
        email='admin@foodmenu.com',
        password_hash=generate_password_hash('admin123'),
        role='admin',
        phone_number='1234567890'
    )
    
    db.session.add(admin)
    db.session.commit()
    print('Admin user created successfully!')
    print('Username: admin')
    print('Password: admin123')

@app.cli.command()
def seed_data():
    """Seed the database with sample menu data"""
    from werkzeug.security import generate_password_hash
    
    # Create categories
    categories = [
        Category(name='Appetizers', description='Start your meal with these delicious bites', display_order=1),
        Category(name='Main Courses', description='Hearty and satisfying main dishes', display_order=2),
        Category(name='Desserts', description='Sweet treats to end your meal', display_order=3),
        Category(name='Beverages', description='Refreshing drinks and beverages', display_order=4),
    ]
    
    for category in categories:
        db.session.add(category)
    
    db.session.commit()
    
    # Create menu items
    menu_items = [
        # Appetizers
        MenuItem(name='Garlic Bread', description='Crispy bread with garlic butter and herbs', 
                price=5.99, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=10),
        MenuItem(name='Caesar Salad', description='Fresh romaine lettuce with parmesan and croutons', 
                price=8.99, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=15),
        MenuItem(name='Buffalo Wings', description='Spicy chicken wings with blue cheese dip', 
                price=12.99, category_id=1, is_available=True, dietary_tags='spicy', preparation_time=20),
        MenuItem(name='Mozzarella Sticks', description='Golden fried mozzarella with marinara sauce', 
                price=7.99, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=12),
        
        # Main Courses
        MenuItem(name='Margherita Pizza', description='Classic pizza with tomato, mozzarella, and basil', 
                price=14.99, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=25),
        MenuItem(name='Grilled Salmon', description='Fresh Atlantic salmon with lemon butter sauce', 
                price=24.99, category_id=2, is_available=True, dietary_tags='gluten-free', preparation_time=30),
        MenuItem(name='Beef Burger', description='Juicy beef patty with lettuce, tomato, and fries', 
                price=16.99, category_id=2, is_available=True, dietary_tags='', preparation_time=20),
        MenuItem(name='Chicken Pasta', description='Creamy Alfredo pasta with grilled chicken', 
                price=18.99, category_id=2, is_available=True, dietary_tags='', preparation_time=25),
        MenuItem(name='Veggie Stir Fry', description='Fresh vegetables in savory Asian sauce with rice', 
                price=13.99, category_id=2, is_available=True, dietary_tags='vegan,gluten-free', preparation_time=20),
        
        # Desserts
        MenuItem(name='Chocolate Cake', description='Rich chocolate layer cake with ganache', 
                price=7.99, category_id=3, is_available=True, dietary_tags='vegetarian', preparation_time=5),
        MenuItem(name='Tiramisu', description='Classic Italian coffee-flavored dessert', 
                price=8.99, category_id=3, is_available=True, dietary_tags='vegetarian', preparation_time=5),
        MenuItem(name='Ice Cream Sundae', description='Vanilla ice cream with toppings of your choice', 
                price=6.99, category_id=3, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5),
        
        # Beverages
        MenuItem(name='Fresh Lemonade', description='Homemade lemonade with fresh lemons', 
                price=3.99, category_id=4, is_available=True, dietary_tags='vegan,gluten-free', preparation_time=5),
        MenuItem(name='Iced Coffee', description='Cold brew coffee with ice', 
                price=4.99, category_id=4, is_available=True, dietary_tags='vegan', preparation_time=5),
        MenuItem(name='Mango Smoothie', description='Fresh mango blended with yogurt', 
                price=5.99, category_id=4, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5),
    ]
    
    for item in menu_items:
        db.session.add(item)
    
    db.session.commit()
    
    print('Database seeded successfully!')
    print(f'Created {len(categories)} categories and {len(menu_items)} menu items')

if __name__ == '__main__':
    app.run(debug=True)
