"""
Script to update the database with Indian menu items
"""
from app import create_app, db
from app.models import Category, MenuItem
import os

app = create_app()

with app.app_context():
    # Clear existing data
    print('Clearing existing menu data...')
    MenuItem.query.delete()
    Category.query.delete()
    db.session.commit()
    print('✓ Cleared!')
    
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
    
    # Create menu items with sample images
    print('\nCreating menu items...')
    menu_items = [
        # Starters
        MenuItem(name='Samosa', description='Crispy pastry filled with spiced potatoes and peas', 
                price=60.00, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=15,
                image_url='https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400'),
        MenuItem(name='Paneer Tikka', description='Grilled cottage cheese cubes marinated in spices', 
                price=180.00, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=20,
                image_url='https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400'),
        MenuItem(name='Chicken 65', description='Spicy and tangy deep-fried chicken appetizer', 
                price=220.00, category_id=1, is_available=True, dietary_tags='spicy', preparation_time=25,
                image_url='https://images.unsplash.com/photo-1610057099443-fde8c4d50f91?w=400'),
        MenuItem(name='Pani Puri', description='Crispy puris filled with spicy tangy water', 
                price=50.00, category_id=1, is_available=True, dietary_tags='vegetarian', preparation_time=10,
                image_url='https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=400'),
        MenuItem(name='Aloo Tikki', description='Crispy potato patties served with chutneys', 
                price=80.00, category_id=1, is_available=True, dietary_tags='vegetarian,vegan', preparation_time=15,
                image_url='https://images.unsplash.com/photo-1626132647523-66f0bf380027?w=400'),
        
        # Main Course
        MenuItem(name='Butter Chicken', description='Creamy tomato-based curry with tender chicken', 
                price=320.00, category_id=2, is_available=True, dietary_tags='', preparation_time=30,
                image_url='https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400'),
        MenuItem(name='Paneer Butter Masala', description='Cottage cheese in rich creamy tomato gravy', 
                price=280.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=25,
                image_url='https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=400'),
        MenuItem(name='Dal Makhani', description='Slow-cooked black lentils in creamy gravy', 
                price=240.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=35,
                image_url='https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400'),
        MenuItem(name='Chicken Biryani', description='Aromatic basmati rice layered with spiced chicken', 
                price=280.00, category_id=2, is_available=True, dietary_tags='', preparation_time=40,
                image_url='https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400'),
        MenuItem(name='Palak Paneer', description='Cottage cheese cooked in spinach gravy', 
                price=260.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=25,
                image_url='https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400'),
        MenuItem(name='Chole Bhature', description='Spicy chickpea curry with fluffy fried bread', 
                price=180.00, category_id=2, is_available=True, dietary_tags='vegetarian', preparation_time=30,
                image_url='https://images.unsplash.com/photo-1626132647523-66f0bf380027?w=400'),
        MenuItem(name='Fish Curry', description='Fresh fish cooked in aromatic coconut curry', 
                price=350.00, category_id=2, is_available=True, dietary_tags='', preparation_time=30,
                image_url='https://images.unsplash.com/photo-1615361200098-635cff16f2c0?w=400'),
        
        # Breads & Rice
        MenuItem(name='Butter Naan', description='Soft leavened bread brushed with butter', 
                price=50.00, category_id=3, is_available=True, dietary_tags='vegetarian', preparation_time=10,
                image_url='https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400'),
        MenuItem(name='Garlic Naan', description='Naan bread topped with garlic and cilantro', 
                price=60.00, category_id=3, is_available=True, dietary_tags='vegetarian', preparation_time=12,
                image_url='https://images.unsplash.com/photo-1619887261115-bbb8d2f73a04?w=400'),
        MenuItem(name='Tandoori Roti', description='Whole wheat flatbread from clay oven', 
                price=30.00, category_id=3, is_available=True, dietary_tags='vegetarian,vegan', preparation_time=10,
                image_url='https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400'),
        MenuItem(name='Jeera Rice', description='Basmati rice tempered with cumin seeds', 
                price=120.00, category_id=3, is_available=True, dietary_tags='vegetarian,vegan,gluten-free', preparation_time=20,
                image_url='https://images.unsplash.com/photo-1596560548464-f010549b84d7?w=400'),
        MenuItem(name='Veg Pulao', description='Fragrant rice cooked with mixed vegetables', 
                price=160.00, category_id=3, is_available=True, dietary_tags='vegetarian,vegan,gluten-free', preparation_time=25,
                image_url='https://images.unsplash.com/photo-1645177628172-a94c30a5314f?w=400'),
        
        # Desserts
        MenuItem(name='Gulab Jamun', description='Soft milk dumplings soaked in sugar syrup', 
                price=80.00, category_id=4, is_available=True, dietary_tags='vegetarian', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1589119908995-f474bff05909?w=400'),
        MenuItem(name='Rasmalai', description='Cottage cheese patties in sweetened milk', 
                price=100.00, category_id=4, is_available=True, dietary_tags='vegetarian', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1582441929850-ff2f1b47e207?w=400'),
        MenuItem(name='Kheer', description='Traditional rice pudding with cardamom', 
                price=90.00, category_id=4, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400'),
        MenuItem(name='Gajar Halwa', description='Sweet carrot pudding with nuts and ghee', 
                price=110.00, category_id=4, is_available=True, dietary_tags='vegetarian', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=400'),
        
        # Beverages
        MenuItem(name='Masala Chai', description='Spiced Indian tea with milk', 
                price=40.00, category_id=5, is_available=True, dietary_tags='vegetarian', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=400'),
        MenuItem(name='Lassi', description='Traditional yogurt-based drink - Sweet or Salted', 
                price=60.00, category_id=5, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1608242155359-d33e08f04e5e?w=400'),
        MenuItem(name='Mango Lassi', description='Refreshing yogurt drink with mango pulp', 
                price=80.00, category_id=5, is_available=True, dietary_tags='vegetarian,gluten-free', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1631451095765-2c91616fc9e6?w=400'),
        MenuItem(name='Fresh Lime Soda', description='Tangy lime juice with soda - Sweet or Salted', 
                price=50.00, category_id=5, is_available=True, dietary_tags='vegan,gluten-free', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1546173159-315724a31696?w=400'),
        MenuItem(name='Filter Coffee', description='South Indian style filter coffee', 
                price=50.00, category_id=5, is_available=True, dietary_tags='vegetarian', preparation_time=5,
                image_url='https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400'),
    ]
    
    for item in menu_items:
        db.session.add(item)
    
    db.session.commit()
    
    print(f'✓ Created {len(menu_items)} Indian menu items with images!')
    print('\n' + '='*50)
    print('✅ INDIAN MENU UPDATE COMPLETE!')
    print('='*50)
    print('\nRestart your Flask server to see the changes!')
    print('All prices are in INR (₹)')
