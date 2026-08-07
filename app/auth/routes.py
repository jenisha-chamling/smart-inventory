from flask import render_template, redirect, url_for, flash

from . import auth
from app.forms import RegisterForm
from app.models import User
from app import db


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_user:
            flash("Email already registered.", "danger")
            return render_template(
                "auth/register.html",
                form=form
            )

        user = User(
            full_name=form.full_name.data,
            email=form.email.data
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration successful! Please login.",
            "success"
        )

        return redirect(url_for("auth.register"))

    return render_template(
        "auth/register.html",
        form=form
    )