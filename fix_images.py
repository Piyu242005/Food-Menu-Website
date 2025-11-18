import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Check all items
cursor.execute('SELECT id, name, image_url FROM menu_items')
items = cursor.fetchall()

print("Items without images:")
for item in items:
    if not item[2]:
        print(f"  - {item[1]} (ID: {item[0]})")

# Update missing images with Unsplash URLs
updates = [
    (1, "Samosa", "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800"),
    (2, "Paneer Tikka", "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=800"),
    (3, "Chicken 65", "https://images.unsplash.com/photo-1610057099443-fde8c4d50f91?w=800"),
    (4, "Pani Puri", "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800"),
    (5, "Aloo Tikki", "https://images.unsplash.com/photo-1626132647523-66f0bf380027?w=800"),
    (6, "Butter Chicken", "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800"),
    (7, "Palak Paneer", "https://images.unsplash.com/photo-1645177628172-a94c30a5e67e?w=800"),
    (8, "Dal Makhani", "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=800"),
    (9, "Biryani", "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800"),
    (10, "Chole Bhature", "https://images.unsplash.com/photo-1626074353765-517a681e40be?w=800"),
    (11, "Fish Curry", "https://images.unsplash.com/photo-1626074353031-e0fbeb78d2c6?w=800"),
    (12, "Naan", "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=800"),
    (13, "Garlic Naan", "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=800"),
    (14, "Tandoori Roti", "https://images.unsplash.com/photo-1619871196041-f9c5222a5b3b?w=800"),
    (15, "Jeera Rice", "https://images.unsplash.com/photo-1596560548464-f010549b84d7?w=800"),
    (16, "Veg Pulao", "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=800"),
    (17, "Gulab Jamun", "https://images.unsplash.com/photo-1590301157890-4810ed352733?w=800"),
    (18, "Rasmalai", "https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=800"),
    (19, "Kheer", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800"),
    (20, "Gajar Halwa", "https://images.unsplash.com/photo-1589301773859-bb024d3f4e4a?w=800"),
    (21, "Kulfi", "https://images.unsplash.com/photo-1631729371254-42c2892f0e6e?w=800"),
    (22, "Masala Chai", "https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=800"),
    (23, "Lassi", "https://images.unsplash.com/photo-1623065422902-30a2d299bbe4?w=800"),
    (24, "Mango Lassi", "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800"),
    (25, "Nimbu Pani", "https://images.unsplash.com/photo-1523677011781-c91d1bbe2f9f?w=800"),
    (26, "Fresh Coconut Water", "https://images.unsplash.com/photo-1551024739-14e1f532e4c6?w=800"),
]

for item_id, name, image_url in updates:
    cursor.execute('UPDATE menu_items SET image_url = ? WHERE id = ?', (image_url, item_id))
    print(f"Updated {name} with image")

conn.commit()
conn.close()
print("\nAll images updated!")
