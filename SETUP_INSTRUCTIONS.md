# Food Menu Website - Setup and Run Instructions

## Quick Start Guide

### Step 1: Create Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 3: Initialize Database
```powershell
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Step 4: Seed Sample Data
```powershell
flask seed-data
flask create-admin
```

### Step 5: Run Application
```powershell
python run.py
```

### Step 6: Open in Browser
Navigate to: http://localhost:5000

## Default Admin Credentials
- Username: `admin`
- Password: `admin123`

## Features Implemented

### Customer Features
- ✅ Browse menu by categories
- ✅ Search and filter items
- ✅ Add items to cart
- ✅ User registration and login
- ✅ Place orders with delivery details
- ✅ View order history
- ✅ Responsive design

### Admin Features
- ✅ Admin dashboard with statistics
- ✅ Add/edit/delete menu items
- ✅ Manage categories
- ✅ View and manage orders
- ✅ Update order status
- ✅ Upload food images

### Technical Features
- ✅ Flask 3.0 with blueprints
- ✅ SQLAlchemy ORM
- ✅ Flask-Login authentication
- ✅ Flask-WTF forms with CSRF protection
- ✅ Tailwind CSS modern UI
- ✅ Alpine.js for interactivity
- ✅ Session-based shopping cart
- ✅ Password hashing
- ✅ File upload support

## Project Structure

```
app/
├── __init__.py           # Flask app factory
├── models.py             # Database models
├── forms.py              # WTForms
├── main/                 # Public routes
├── auth/                 # Authentication
├── cart/                 # Shopping cart
├── admin/                # Admin panel
├── templates/            # Jinja2 templates
└── static/               # Static assets
```

## Database Models

1. **User** - Authentication and profiles
2. **Category** - Menu categories
3. **MenuItem** - Food items
4. **Order** - Customer orders
5. **OrderItem** - Order line items

## Routes

### Public Routes
- `/` - Homepage
- `/menu` - Browse menu
- `/menu/item/<id>` - Item details

### Auth Routes
- `/auth/login` - User login
- `/auth/register` - User registration
- `/auth/profile` - User profile
- `/auth/logout` - Logout

### Cart Routes
- `/cart` - View cart
- `/cart/add/<id>` - Add to cart
- `/cart/checkout` - Checkout
- `/cart/order/<id>` - Order confirmation

### Admin Routes (Requires admin role)
- `/admin` - Dashboard
- `/admin/menu-items` - Manage menu
- `/admin/categories` - Manage categories
- `/admin/orders` - Manage orders

## Environment Variables

Create a `.env` file (already created):
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///instance/database.db
UPLOAD_FOLDER=app/static/uploads
MAX_CONTENT_LENGTH=16777216
```

## Tips

1. **Test as Customer:**
   - Register a new account
   - Browse menu and add items
   - Complete checkout
   - View order in profile

2. **Test as Admin:**
   - Login with admin credentials
   - Add menu items with images
   - Manage orders
   - Update order status

3. **Development:**
   - Debug mode is enabled by default
   - Changes to templates reload automatically
   - Check console for errors

## Troubleshooting

**Issue:** Database doesn't exist
**Solution:** Run `flask db upgrade`

**Issue:** Import errors
**Solution:** Activate virtual environment first

**Issue:** Port 5000 in use
**Solution:** Change port in `run.py` or stop other Flask apps

## Next Steps for Production

1. Change `SECRET_KEY` to a secure random string
2. Set `FLASK_ENV=production`
3. Use PostgreSQL instead of SQLite
4. Set up proper file storage (AWS S3)
5. Add payment gateway integration
6. Configure email service
7. Add SSL certificate
8. Set up logging and monitoring

## Technologies Used

- **Backend:** Python 3.10+, Flask 3.0
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Frontend:** HTML5, Tailwind CSS 3.x, Alpine.js
- **Authentication:** Flask-Login
- **Forms:** Flask-WTF, WTForms
- **Migrations:** Flask-Migrate

Enjoy your Food Menu Website! 🍕🍔🍰
