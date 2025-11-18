"""
WTForms Forms for validation
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField, FloatField, SelectField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, NumberRange, Optional
from app.models import User

class LoginForm(FlaskForm):
    """User login form"""
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    """User registration form"""
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different one.')

class CheckoutForm(FlaskForm):
    """Checkout form"""
    customer_name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    customer_email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=20)])
    delivery_address = TextAreaField('Delivery Address', validators=[DataRequired()])
    special_instructions = TextAreaField('Special Instructions (Optional)', validators=[Optional()])
    payment_method = SelectField('Payment Method', choices=[
        ('cash', 'Cash on Delivery'),
        ('card', 'Credit/Debit Card'),
        ('online', 'Online Payment')
    ], validators=[DataRequired()])

class MenuItemForm(FlaskForm):
    """Form for adding/editing menu items"""
    name = StringField('Item Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[Optional()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    dietary_tags = StringField('Dietary Tags (comma separated)', validators=[Optional(), Length(max=255)])
    preparation_time = IntegerField('Preparation Time (minutes)', validators=[Optional(), NumberRange(min=0)])
    is_available = BooleanField('Available')
    image = FileField('Item Image', validators=[Optional(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])

class CategoryForm(FlaskForm):
    """Form for adding/editing categories"""
    name = StringField('Category Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[Optional()])
    display_order = IntegerField('Display Order', validators=[Optional(), NumberRange(min=0)])

class ProfileForm(FlaskForm):
    """User profile edit form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    address = TextAreaField('Default Delivery Address', validators=[Optional()])
