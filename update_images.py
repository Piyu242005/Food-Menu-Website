import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Update with correct Unsplash and other image URLs
updates = [
    ('Aloo Tikki', 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800'),
    ('Paneer Tikka', 'https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=800'),
    ('Paneer Butter Masala', 'https://images.unsplash.com/photo-1666190090242-a1c5e2b07305?w=800'),
    ('Chole Bhature', 'https://static.vecteezy.com/system/resources/previews/015/933/617/non_2x/chole-bhature-is-a-north-indian-food-dish-a-combination-of-chana-masala-and-bhatura-or-puri-free-photo.jpg'),
    ('Garlic Naan', 'https://images.unsplash.com/photo-1571676165119-62f85d007a22?w=800'),
    ('Kheer', 'https://img.freepik.com/free-photo/semiya-payasam-shewai-sewai-khir-seviyan-kheer-is-indian-sweet-made-with-vermicelli-milk-ghee-sugar-jaggery-raisins-nuts_466689-76842.jpg'),
    ('Nimbu Pani', 'https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=800'),
    ('Filter Coffee', 'https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?w=800'),
]

for name, image_url in updates:
    cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', (image_url, name))
    print(f'Updated {name}')

# Also update some other items with better Unsplash URLs
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800', 'Samosa'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800', 'Butter Chicken'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1645177628172-a94c30a5e67e?w=800', 'Palak Paneer'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=800', 'Dal Makhani'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800', 'Biryani'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1626074353031-e0fbeb78d2c6?w=800', 'Fish Curry'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1628840042765-356cda07504e?w=800', 'Naan'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1619871196041-f9c5222a5b3b?w=800', 'Tandoori Roti'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1596560548464-f010549b84d7?w=800', 'Jeera Rice'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=800', 'Veg Pulao'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1590301157890-4810ed352733?w=800', 'Gulab Jamun'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=800', 'Rasmalai'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1589301773859-bb024d3f4e4a?w=800', 'Gajar Halwa'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1631729371254-42c2892f0e6e?w=800', 'Kulfi'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=800', 'Masala Chai'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1623065422902-30a2d299bbe4?w=800', 'Lassi'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800', 'Mango Lassi'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1551024739-14e1f532e4c6?w=800', 'Fresh Coconut Water'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800', 'Pani Puri'))
cursor.execute('UPDATE menu_items SET image_url = ? WHERE name = ?', 
               ('https://images.unsplash.com/photo-1610057099443-fde8c4d50f91?w=800', 'Chicken 65'))

conn.commit()
conn.close()

print('\nAll images updated successfully!')
