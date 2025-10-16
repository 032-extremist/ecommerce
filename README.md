# CodeAlpha_ecommerce Store
A simple e-commerce web application built with Django backend and vanilla JavaScript frontend.

Features
Product Catalog: Browse products with categories and search

Shopping Cart: Add/remove items, update quantities

User Authentication: Registration and login system

Order Management: Process and track orders

Responsive Design: Works on desktop and mobile devices

Tech Stack
Backend
Django - Python web framework

Django REST Framework - API development

SQLite - Database (default, can be changed to PostgreSQL/MySQL)

Frontend
HTML5 - Structure

CSS3 - Styling with CSS Grid and Flexbox

Vanilla JavaScript - Client-side functionality

Local Storage - Cart persistence

Project Structure
text
ecommerce/
├── backend/
│   ├── ecommerce/          # Project settings
│   ├── store/              # Products and categories
│   ├── orders/             # Order management
│   ├── users/              # Authentication
│   └── manage.py
├── frontend/
│   └── ecommerce.html      # Main frontend file
└── README.md
Installation & Setup
Prerequisites
Python 3.8+

pip (Python package manager)

Backend Setup
Clone or create the project directory

bash
cd ecommerce
Create virtual environment

bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
Install dependencies

bash
pip install django djangorestframework pillow django-cors-headers
Run migrations

bash
python manage.py makemigrations
python manage.py migrate
Create superuser

bash
python manage.py createsuperuser
Start development server

bash
python manage.py runserver
Frontend Setup
Open the frontend

Simply open ecommerce.html in your web browser

Or serve it using a local server:

bash
python -m http.server 3000  # Then visit http://localhost:3000
API Endpoints
Endpoint	Method	Description
/api/products/	GET	List all products
/api/categories/	GET	List all categories
/api/orders/	GET, POST	User orders
/api/auth/register/	POST	User registration
/api/auth/login/	POST	User login
Usage
Access the application: Open ecommerce.html in your browser

Browse products: Click on "Products" to view available items

Add to cart: Click "Add to Cart" on any product

View cart: Click "Cart" to see selected items

Register/Login: Create an account or login to place orders

Checkout: Proceed to checkout to complete your order

Admin Panel
Access the Django admin panel at: http://localhost:8000/admin/

Add products and categories

Manage orders and users

Monitor inventory

Configuration
Backend Settings (ecommerce/settings.py)
Key configurations:

python
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
CORS_ALLOW_ALL_ORIGINS = True  # For development
Frontend Configuration
Update API base URL in JavaScript if needed:

javascript
const API_BASE = 'http://localhost:8000/api';
Development
Adding New Features
Backend:

Create models in appropriate app

Add serializers for API

Create views and URL routes

Run migrations

Frontend:

Update HTML structure

Add CSS styles

Implement JavaScript functionality

Test API integration

Testing
Backend: Use Django test framework

Frontend: Manual testing in browser

API testing: Use browser or tools like Postman

Deployment
Backend (Production)
Set DEBUG = False

Configure production database (PostgreSQL recommended)

Set up static files serving

Use production WSGI server (Gunicorn)

Configure web server (Nginx/Apache)

Frontend (Production)
Minify CSS and JavaScript

Optimize images

Serve via CDN or web server

Troubleshooting
Common Issues
CORS Errors:

Install django-cors-headers

Configure CORS settings in settings.py

API Connection Failed:

Ensure Django server is running on port 8000

Check browser console for errors

Verify API endpoints are correct

Static Files Not Loading:

Run python manage.py collectstatic

Check static files configuration

Contributing
Fork the project

Create a feature branch

Make changes

Test thoroughly

Submit pull request

License
This project is for educational purposes as part of the CodeAlpha internship program.

Support
For issues and questions:

Check the troubleshooting section

Review Django and JavaScript documentation

Contact the development team

Note: This is a learning project. For production use, implement proper security measures, input validation, and error handling.
