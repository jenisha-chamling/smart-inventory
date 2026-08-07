from flask_wtf import FlaskForm
from wtforms import SelectField

from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    TextAreaField,
    IntegerField,
    DecimalField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
    Optional
)


class RegisterForm(FlaskForm):

    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match."
            )
        ]
    )

    submit = SubmitField(
        "Create Account"
    )


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Login"
    )


class SupplierForm(FlaskForm):

    name = StringField(
        "Supplier Name",
        validators=[
            DataRequired(),
            Length(min=2, max=150)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            Optional(),
            Email()
        ]
    )

    phone = StringField(
        "Phone",
        validators=[
            Optional(),
            Length(max=30)
        ]
    )

    address = StringField(
        "Address",
        validators=[
            Optional(),
            Length(max=255)
        ]
    )

    contact_person = StringField(
        "Contact Person",
        validators=[
            Optional(),
            Length(max=100)
        ]
    )

    submit = SubmitField(
        "Save Supplier"
    )


class ProductForm(FlaskForm):

    name = StringField(
        "Product Name",
        validators=[DataRequired()]
    )

    sku = StringField(
        "SKU",
        validators=[DataRequired()]
    )

    description = TextAreaField(
        "Description",
        validators=[Optional()]
    )

    quantity = IntegerField(
        "Quantity",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    price = DecimalField(
        "Price",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ],
        places=2
    )

    reorder_level = IntegerField(
        "Reorder Level",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    supplier_id = SelectField(
        "Supplier",
        coerce=int,
        validators=[Optional()]
    )

    submit = SubmitField("Save Product")