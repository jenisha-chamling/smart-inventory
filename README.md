# Smart Inventory Management System

## Overview

Smart Inventory Management System is a web-based inventory management application developed using Python, Flask, MySQL, SQLAlchemy, and Bootstrap.

The project is designed using a modular Flask application structure to separate authentication, dashboard, product management, and supplier management functionality.

The primary objective of the project is to develop a maintainable and scalable inventory management application while applying software engineering concepts such as:

- Modular application architecture
- Database-driven application development
- CRUD operations
- User authentication and authorization
- Form validation
- Database migrations
- Separation of concerns
- Reusable templates
- Secure configuration management
- Error handling and user feedback

The current implementation focuses on the core functionality required to manage users, suppliers, and products.

---

## Key Features

### User Authentication

The application provides a complete authentication workflow using Flask-Login.

Implemented functionality includes:

- User registration
- User login
- User logout
- Session-based authentication
- Protection of authenticated routes
- Redirecting unauthenticated users to the login page
- Displaying authentication-related feedback messages

Authenticated users can access protected application modules such as products and suppliers.

---

### Dashboard

The dashboard provides a centralized entry point for authenticated users.

It provides navigation to the main modules currently implemented in the system, including:

- Dashboard
- Products
- Suppliers
- Home
- Logout

The dashboard structure is designed so that additional inventory-related functionality can be integrated later without significantly changing the existing application architecture.

---

### Supplier Management

The supplier module provides functionality for managing supplier information.

Implemented operations include:

- Creating suppliers
- Viewing suppliers
- Editing supplier information
- Deleting suppliers

The supplier module follows Flask's Blueprint-based organization, keeping supplier-related routes separate from other application functionality.

This modular approach improves code organization and makes the application easier to maintain and extend.

---

### Product Management

The product module provides the core inventory management functionality currently implemented in the system.

Users can:

- Add products
- View products
- Edit products
- Delete products
- Assign suppliers to products
- Manage product SKU
- Manage product quantity
- Manage product price
- Define product reorder levels

The product listing displays important inventory information such as:

- Product name
- SKU
- Supplier
- Quantity
- Price
- Reorder level
- Stock status

---

### Stock-Level Monitoring

The system includes basic inventory status monitoring using product quantity and reorder level.

The application compares the current quantity of a product with its defined reorder level.

The logic is:

    If quantity <= reorder level
        → Low Stock

    If quantity > reorder level
        → In Stock

This provides users with a simple way to identify products that may require restocking.

---

# Software Engineering Implementation

The project is developed with software engineering principles in mind rather than implementing all functionality in a single Flask file.

## Modular Application Design

The application separates major functionality into independent Flask Blueprints.

The completed modules include:

### `app/auth/`

This module contains authentication-related functionality.

It is responsible for:

- Registration
- Login
- Logout
- Authentication-related routes

Separating authentication into its own module improves maintainability and allows authentication functionality to be modified without affecting product or supplier logic.

---

### `app/dashboard/`

This module contains dashboard-related functionality.

It provides the authenticated user with a central interface for accessing the application's major modules.

The dashboard is separated from other application functionality to maintain a clear separation of responsibilities.

---

### `app/products/`

This module handles product and inventory-related operations.

It contains routes responsible for:

- Listing products
- Adding products
- Editing products
- Deleting products

The module also handles supplier assignment and stock-level information associated with products.

---

### `app/suppliers/`

This module handles supplier management.

It contains functionality for:

- Listing suppliers
- Adding suppliers
- Editing suppliers
- Deleting suppliers

Supplier functionality is kept separate from product functionality while still allowing products to reference suppliers through the database relationship.

---

## Application Core

### `app/__init__.py`

This file contains the Flask application factory and initializes the major Flask extensions used by the project.

The application factory pattern is used through:

    create_app()

The application initializes:

- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-Login

It also registers the application's Blueprints.

Using an application factory makes the application easier to configure, test, and extend.

---

### `app/config.py`

This file contains application configuration.

Environment variables are loaded using `python-dotenv`.

Database configuration and the Flask secret key are kept outside the source code through environment variables.

This approach prevents sensitive configuration values from being hard-coded directly into the application.

---

### `app/models.py`

This file contains the SQLAlchemy database models.

The User model stores user-related information required for authentication.

The project also uses database models for product and supplier management.

SQLAlchemy provides an ORM-based approach for interacting with the MySQL database instead of writing raw SQL queries throughout the application.

---

### `app/forms.py`

This file contains the application's form classes.

Forms are used for handling user input and validating submitted data.

The completed application uses forms for areas such as:

- User registration
- User login
- Product creation and editing
- Supplier-related input

Using dedicated form classes keeps validation logic separate from route logic and improves code maintainability.

---

## Templates

The application uses Jinja2 templates with a reusable layout system.

The main completed template areas are:

### `app/templates/auth/`

Contains authentication-related pages such as:

- Registration
- Login

---

### `app/templates/dashboard/`

Contains dashboard-related templates.

The dashboard provides a centralized interface for authenticated users.

---

### `app/templates/products/`

Contains product management pages such as:

- Product listing
- Add product
- Edit product

These templates use reusable form and layout patterns to reduce duplication.

---

### `app/templates/suppliers/`

Contains supplier management pages.

These templates provide interfaces for viewing and managing supplier information.

---

### `app/templates/layouts/`

Contains reusable application layouts.

The main layout provides common elements such as:

- Navigation bar
- Flash messages
- Bootstrap integration
- Main content area
- Template inheritance

Individual pages extend the base layout rather than duplicating the same HTML structure.

This improves consistency and maintainability across the application.

---

# Database Management

## MySQL

MySQL is used as the primary relational database.

The database stores application data such as:

- Users
- Products
- Suppliers

Relationships between entities are represented using SQLAlchemy models.

For example, products can be associated with suppliers, allowing the system to display the supplier of a particular product.

---

## SQLAlchemy

Flask-SQLAlchemy is used as the ORM layer.

It provides:

- Model-based database design
- Database queries
- Relationships between entities
- CRUD operations
- Session management

This allows application logic to interact with the database using Python objects and SQLAlchemy queries.

---

## Database Migrations

Flask-Migrate is used to manage database schema changes.

The migration workflow used in the project includes:

    flask db migrate -m "Migration message"

and:

    flask db upgrade

This provides a controlled way to apply database structure changes without manually recreating the database.

The `migrations/` directory stores the generated migration history.

---

# Authentication and Security

Flask-Login is used to manage user sessions.

Protected routes use:

    @login_required

This ensures that only authenticated users can access protected functionality.

The application also uses:

- Password handling
- Session-based authentication
- CSRF protection for forms
- Environment variables for sensitive configuration
- Login redirects for unauthorized access

Sensitive database credentials are stored in `.env` rather than being directly written into the application source code.

---

# Validation and Error Handling

The application performs validation before processing submitted forms.

Examples include:

- Checking whether an email is already registered
- Checking whether a product SKU already exists
- Validating product information
- Validating supplier information
- Handling missing database records

The application uses Flask's `flash()` mechanism to provide feedback to users after operations.

Examples include:

- Successful registration
- Successful product creation
- Successful product update
- Successful deletion
- Invalid login credentials
- Duplicate product SKU
- Duplicate email registration

This provides users with clear feedback about the result of their actions.

---

# CRUD Operations

The project demonstrates complete CRUD functionality for the main management entities.

CRUD stands for:

- **Create** – Add a new record
- **Read** – View existing records
- **Update** – Modify an existing record
- **Delete** – Remove a record

The completed product and supplier modules use these operations to manage inventory-related data.

---

# Frontend

The application uses:

- HTML5
- Jinja2
- Bootstrap 5

Bootstrap is currently used through its CDN integration.

The reusable base template provides a consistent navigation system and page layout across the application.

The interface includes responsive navigation and Bootstrap components such as:

- Navigation bars
- Buttons
- Tables
- Forms
- Cards
- Alerts
- Badges

---

# Application Workflow

The current application workflow is:

    User
      |
      v
    Register
      |
      v
    Login
      |
      v
    Dashboard
      |
      +-------------------+
      |                   |
      v                   v
    Suppliers          Products
      |                   |
      |                   +--> Add Product
      |                   |
      |                   +--> View Products
      |                   |
      |                   +--> Edit Product
      |                   |
      |                   +--> Delete Product
      |
      +--> Add Supplier
      |
      +--> View Suppliers
      |
      +--> Edit Supplier
      |
      +--> Delete Supplier

---

# Technologies Used

## Backend

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF / WTForms

## Frontend

- HTML5
- Jinja2
- Bootstrap 5

## Database

- MySQL
- PyMySQL

## Development

- Python Virtual Environment
- Flask CLI
- Git
- GitHub

---

# Environment Configuration

The application uses a `.env` file for sensitive configuration.

Example:

    SECRET_KEY=your_secret_key

    DB_USER=root
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=smart_inventory

Actual credentials should never be committed to the repository.

The `.env` file should be included in `.gitignore`.

---

# Installation

## 1. Create a Virtual Environment

    python -m venv venv

Activate the environment on Windows:

    venv\Scripts\activate

---

## 2. Install Dependencies

    pip install -r requirements.txt

---

## 3. Configure Environment Variables

Create a `.env` file and configure the required database and application settings.

---

## 4. Configure MySQL

Create the required MySQL database and ensure that the credentials in `.env` match the database configuration.

---

## 5. Apply Database Migrations

Run:

    flask db upgrade

If new model changes are introduced:

    flask db migrate -m "Describe the change"

    flask db upgrade

---

## 6. Run the Application

    python run.py

The application will normally be available at:

    http://127.0.0.1:5000

---

# Development Practices Demonstrated

This project demonstrates practical software engineering concepts including:

- Modular Flask architecture
- Blueprint-based application organization
- Application factory pattern
- Separation of concerns
- ORM-based database access
- Database relationships
- CRUD implementation
- Form validation
- Authentication and authorization
- Database migration management
- Reusable template inheritance
- Environment-based configuration
- Error handling
- User feedback through flash messages
- Protected application routes

These practices make the application easier to understand, maintain, test, and extend.

---

# Testing

A `tests/` directory is included for application testing.

Testing can be expanded to cover:

- Authentication
- Form validation
- Product CRUD operations
- Supplier CRUD operations
- Protected routes
- Database operations

The test structure provides a foundation for implementing automated testing as the project continues to grow.

---

# Current Status

The current version implements the core inventory management functionality, including:

- User authentication
- Dashboard
- Supplier management
- Product management
- Supplier-product relationship
- Inventory quantity tracking
- Reorder-level monitoring
- CRUD operations
- Database migrations
- Protected routes

The application is currently focused on the core inventory and administration workflow.

---

# Future Improvements

Possible future improvements include:

- Inventory transaction management
- Sales management
- Reports and analytics
- Advanced dashboard statistics
- Product search and filtering
- Pagination
- Role-based access control
- Admin and staff roles
- Automated testing
- API development
- Inventory notifications
- Report export functionality

---

# Author

**Jenisha**

BSc CSIT Student

---

# License

This project was developed for educational and software engineering learning purposes.