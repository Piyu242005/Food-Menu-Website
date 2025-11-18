"""
One-time setup script to initialize the database and seed sample data
"""
from app import create_app, db
from app.models import User, Category, MenuItem
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Create all tables
    print('Creating database tables...')
    db.create_all()
    print('✓ Tables created successfully!')
    
    # Check if data already exists
    if Category.query.first():
        print('⚠ Database already has data. Skipping seed.')
        exit()
    
    # Create admin user
    print('\nCreating admin user...')
    admin = User(
        username='Piyu',
        email='piyu@foodmenu.com',
        password_hash=generate_password_hash('Piyu2420'),
        role='admin',
        phone_number='1234567890'
    )
    db.session.add(admin)
    print('✓ Admin user created!')
    print('  Username: Piyu')
    print('  Password: Piyu2420')
    
    # Create categories
    print('\nCreating categories...')
    categories = [
        Category(name='Starters', description='Traditional Indian appetizers and starters', display_order=1),
        Category(name='Main Course', description='Authentic Indian curries and gravies', display_order=2),
        Category(name='Breads & Rice', description='Freshly baked breads and aromatic rice', display_order=3),
        Category(name='Desserts', description='Traditional Indian sweets', display_order=4),
        Category(name='Beverages', description='Refreshing Indian drinks', display_order=5),
    ]
    
    for category in categories:
        db.session.add(category)
    
    db.session.commit()
    print(f'✓ Created {len(categories)} categories!')
    
    # Create menu items
    print('\nCreating menu items...')
    menu_items = [
        # Starters
        MenuItem(name='Samosa', description='Crispy pastry filled with spiced potatoes and peas', 
                price=60.00, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=15),
        MenuItem(name='Paneer Tikka', description='Grilled cottage cheese cubes marinated in spices', 
                price=180.00, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=20),
        MenuItem(name='Chicken 65', description='Spicy and tangy deep-fried chicken appetizer', 
                price=220.00, category_id=1, is_available=True, dietary_tags='spicy', preparation_time=25),
        MenuItem(name='Pani Puri', description='Crispy puris filled with spicy tangy water', 
                price=50.00, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=10),
        MenuItem(name='Aloo Tikki', description='Crispy potato patties served with chutneys', 
                price=80.00, category_id=1, is_available=True, dietary_tags='vegetarian,vegan', preparation_time=15),
        
        # Main Course
        MenuItem(name='Butter Chicken', description='Creamy tomato-based curry with tender chicken', 
                price=320.00, category_id=2, is_available=True, dietary_tags='', preparation_time=30),
        MenuItem(name='Paneer Butter Masala', description='Cottage cheese in rich creamy tomato gravy', 
                price=280.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=25),
        MenuItem(name='Dal Makhani', description='Slow-cooked black lentils in creamy gravy', 
                price=240.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=35),
        MenuItem(name='Chicken Biryani', description='Aromatic basmati rice layered with spiced chicken', 
                price=280.00, category_id=2, is_available=True, dietary_tags='', preparation_time=40),
        MenuItem(name='Palak Paneer', description='Cottage cheese cooked in spinach gravy', 
                price=260.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=25),
        MenuItem(name='Chole Bhature', description='Spicy chickpea curry with fluffy fried bread', 
                price=180.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=30),
        MenuItem(name='Fish Curry', description='Fresh fish cooked in aromatic coconut curry', 
                price=350.00, category_id=2, is_available=True, dietary_tags='', preparation_time=30),
        
        # Breads & Rice
        MenuItem(name='Butter Naan', description='Soft leavened bread brushed with butter', 
                price=50.00, category_id=3, is_available=True, dietary_tags='vegetarian', preparation_time=10),
        MenuItem(name='Garlic Naan', description='Naan bread topped with garlic and cilantro', 
                price=60.00, category_id=3, is_available=True, dietary_tags='vegetarian', preparation_time=12),
        MenuItem(name='Tandoori Roti', description='Whole wheat flatbread from clay oven', 
                price=30.00, category_id=3, is_available=True, dietary_tags='vegetarian,vegan', preparation_time=10),
        MenuItem(name='Jeera Rice', description='Basmati rice tempered with cumin seeds', 
                price=120.00, category_id=3, is_available=True, dietary_tags='vegetarian,vegan,gluten-free', preparation_time=20),
        MenuItem(name='Veg Pulao', description='Fragrant rice cooked with mixed vegetables', 
                price=160.00, category_id=3, is_available=True, dietary_tags='vegetarian,vegan,gluten-free', preparation_time=25),
        
        # Desserts
        MenuItem(name='Gulab Jamun', description='Soft milk dumplings soaked in sugar syrup', 
                price=80.00, category_id=4, is_available=True, dietary_tags='vegetarian', preparation_time=5),
        MenuItem(name='Rasmalai', description='Cottage cheese patties in sweetened milk', 
                price=100.00, category_id=4, is_available=True, dietary_tags='vegetarian', preparation_time=5),
        MenuItem(name='Kheer', description='Traditional rice pudding with cardamom', 
                price=90.00, category_id=4, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5),
        MenuItem(name='Gajar Halwa', description='Sweet carrot pudding with nuts and ghee', 
                price=110.00, category_id=4, is_available=True, dietary_tags='vegetarian', preparation_time=5),
        
        # Beverages
        MenuItem(name='Masala Chai', description='Spiced Indian tea with milk', 
                price=40.00, category_id=5, is_available=True, dietary_tags='vegetarian', preparation_time=5),
        MenuItem(name='Lassi', description='Traditional yogurt-based drink - Sweet or Salted', 
                price=60.00, category_id=5, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5),
        MenuItem(name='Mango Lassi', description='Refreshing yogurt drink with mango pulp', 
                price=80.00, category_id=5, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5),
        MenuItem(name='Fresh Lime Soda', description='Tangy lime juice with soda - Sweet or Salted', 
                price=50.00, category_id=5, is_available=True, dietary_tags='vegan,gluten-free', preparation_time=5),
        MenuItem(name='Filter Coffee', description='South Indian style filter coffee', 
                price=50.00, category_id=5, is_available=True, dietary_tags='vegetarian', preparation_time=5),
    ]
    
    for item in menu_items:
        db.session.add(item)
    
    db.session.commit()
    
    print(f'✓ Created {len(menu_items)} menu items!')
    print('\n' + '='*50)
    print('✅ DATABASE SETUP COMPLETE!')
    print('='*50)
    print('\nYou can now:')
    print('1. Run the app: py run.py')
    print('2. Visit: http://localhost:5000')
    print('3. Login as admin with:')
    print('   - Username: admin')
    print('   - Password: admin123')
    print('\nEnjoy your Food Menu Website! 🍕🍔🍰')
