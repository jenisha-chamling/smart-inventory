# Smart Inventory Management System

A web-based inventory management system developed using **Python, Flask, MySQL, SQLAlchemy, Flask-Login, Flask-WTF, Flask-Migrate, Jinja2, and Bootstrap**.

The system provides authenticated users with a centralized platform to manage products and suppliers, monitor stock levels, and perform basic inventory operations.

---

## Project Overview

The Smart Inventory Management System was developed as a practical software engineering project to demonstrate backend development, database integration, authentication, CRUD operations, form validation, security, and modular application design.

The application follows a modular Flask architecture where authentication, dashboard, products, and suppliers are handled as separate functional components.

---

## Key Features

- User registration and login
- Secure password hashing
- Remember Me functionality
- User logout
- Authentication-based navigation
- Protected application routes
- Dashboard
- Product management
- Supplier management
- Product-supplier relationship
- Stock-level monitoring
- Low-stock detection
- Form validation
- Duplicate SKU validation
- MySQL database integration
- Database migrations
- CSRF protection
- Flash messages
- Responsive Bootstrap interface

---

# Modules

## 1. Main Module

The Main module provides the public home page of the application.

It acts as the initial entry point for users and provides access to authentication features.

Unauthenticated users can access:

```text
Home | Register | Login
2. Authentication Module

The Authentication module manages user accounts and login sessions using Flask-Login.

Registration

Users can create an account using their name, email, and password.

During registration, the application checks whether the email is already registered. Passwords are securely hashed before being stored in the database.

Login

Users can log in using their registered email and password. The system verifies the credentials and creates an authenticated session.

Invalid credentials generate an appropriate error message.

Logout

Authenticated users can log out, ending their authenticated session.

Remember Me

The login form also supports a Remember Me option for maintaining the user's login session.

After login, authenticated users can access:

Home | Dashboard | Products | Suppliers | Logout
3. Dashboard Module

The Dashboard provides the main interface for authenticated users.

It currently displays inventory-related information and provides quick access to common operations.

The Dashboard includes:

Inventory/product information
Supplier information
Low-stock information
Quick Actions
Today's Sales section in the interface
Stock Monitoring

The system determines stock status using the product quantity and reorder level.

Quantity <= Reorder Level → Low Stock
Quantity > Reorder Level  → In Stock

The Dashboard also provides quick actions such as adding products, adding suppliers, and viewing products.

The Sales section is currently part of the Dashboard interface; a separate Sales Management module has not been implemented.

4. Product Management Module

The Product module provides complete CRUD functionality for inventory products.

Users can:

Add products
View products
Edit products
Delete products
Assign suppliers
Set product quantity
Set product price
Set reorder level
Monitor stock status
Product Information

Products contain information such as:

Product ID
Name
SKU
Description
Quantity
Price
Reorder Level
Supplier
Add Product

Before a product is stored, the application validates the submitted form and checks whether the SKU already exists.

This prevents duplicate product identifiers.

Edit Product

Existing products can be updated through a dedicated edit form. During editing, SKU uniqueness is checked while excluding the current product.

Delete Product

Products can be deleted using a POST request with confirmation and CSRF protection.

5. Supplier Management Module

The Supplier module provides CRUD functionality for managing suppliers.

Users can:

Add suppliers
View suppliers
Edit suppliers
Delete suppliers

Suppliers can also be associated with products.

When creating or editing a product, available suppliers are retrieved from the database and displayed as selectable options.

A product can also be saved without a supplier.

6. Database and Models

The application uses MySQL as its relational database and SQLAlchemy as the ORM.

The main database entities implemented are:

User

Stores registered user information and authentication-related data.

Product

Stores product information including name, SKU, quantity, price, reorder level, description, and supplier relationship.

Supplier

Stores supplier information and provides relationships with products.

The general data flow is:

Flask Application
       ↓
SQLAlchemy ORM
       ↓
MySQL Database
7. Forms and Validation

The project uses Flask-WTF and WTForms for form handling and validation.

The implemented forms include:

RegisterForm
LoginForm
ProductForm
SupplierForm

Validation is performed before database operations.

The Product module also implements business validation for duplicate SKUs.

8. Security

Several security practices have been implemented.

Password Hashing

User passwords are hashed instead of being stored as plain text.

CSRF Protection

CSRF tokens are used for state-changing form submissions.

Protected Routes

Features such as Products and Suppliers require authentication using Flask-Login's login_required.

POST for Deletion

Product deletion uses a POST request instead of exposing deletion through a simple GET URL.

9. Application Architecture

The application uses Flask Blueprints to separate functionality into modules:

Main
Authentication
Dashboard
Products
Suppliers

The project also uses the Application Factory pattern to initialize the Flask application and register its components.

This modular structure improves:

Maintainability
Separation of concerns
Debugging
Scalability
Future development
10. Templates and User Interface

The frontend uses HTML, Jinja2, and Bootstrap 5.

A reusable base template is used for common elements such as:

Navigation
Flash messages
Page structure
Content area

Individual pages extend the base template using Jinja2 template inheritance.

The navigation dynamically changes according to the user's authentication state.

Bootstrap components are used for tables, forms, buttons, alerts, cards, and badges.

11. Database Migrations

Flask-Migrate is used to manage database schema changes.

Migration commands include:

flask db migrate -m "Describe change"
flask db upgrade

This allows database changes to be tracked and applied systematically.

12. Error Handling and Debugging

During development, Flask's debugging tools and route inspection were used to identify and resolve issues related to:

Blueprint registration
Template paths
Imports
Authentication
CSRF configuration
Database queries
Jinja2 rendering
Route registration

Registered routes can be verified using:

python -m flask routes

This helped ensure that the application's endpoints were correctly registered.

13. Technology Stack
Technology	Purpose
Python	Backend programming
Flask	Web framework
MySQL	Database
SQLAlchemy	ORM
Flask-Login	Authentication
Flask-WTF / WTForms	Forms and validation
Flask-Migrate	Database migrations
Jinja2	Template engine
Bootstrap 5	User interface
14. Software Engineering Concepts Demonstrated

This project demonstrates practical experience with:

Modular application architecture
Separation of concerns
CRUD operations
Database-driven development
Authentication and session management
Form validation
Database relationships
Password security
CSRF protection
Error handling
Debugging
Template inheritance
Database migrations
Business logic implementation
15. Setup and Installation
Clone the repository
git clone <repository-url>
cd smart_inventory_system
Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Configure MySQL

Create the required MySQL database and configure the application's database connection.

Apply migrations
flask db upgrade
Run the application
python run.py

The application can then be accessed through the local Flask server.

16. Current Project Scope
Completed
Main/Home
User Authentication
Dashboard
Product Management
Supplier Management
Product-Supplier Relationship
Database Integration
Forms and Validation
CRUD Operations
Stock Monitoring
Authentication Protection
CSRF Protection
Password Hashing
Database Migrations
Modular Flask Architecture
Future Enhancements

Potential future additions include:

Sales Management
Advanced Inventory Transactions
Reports
Analytics
Role-Based Access Control
Automated Testing
Search and Filtering
Data Export
Notifications
Author

Jenisha
BSc CSIT — Final Year Student

Developed as a practical software engineering project demonstrating Python/Flask backend development, database management, authentication, CRUD operations, validation, security, and modular application architecture