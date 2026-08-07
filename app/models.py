from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"
  
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    sku = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    price = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    reorder_level = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id"),
        nullable=True
    )

    supplier = db.relationship(
        "Supplier",
        backref="products"
    )

    def __repr__(self):
        return f"<Product {self.name}>"

class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        nullable=True
    )

    phone = db.Column(
        db.String(30),
        nullable=True
    )

    address = db.Column(
        db.String(255),
        nullable=True
    )

    contact_person = db.Column(
        db.String(100),
        nullable=True
    )

    def __repr__(self):
        return f"<Supplier {self.name}>"