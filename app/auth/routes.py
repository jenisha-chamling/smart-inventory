from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required

from . import auth
from app.forms import RegisterForm, LoginForm
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

@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and user.check_password(form.password.data):

            login_user(
                user,
                remember=form.remember.data
            )

            flash(
                f"Welcome back, {user.full_name}!",
                "success"
            )

            return redirect(url_for("main.home"))

        flash(
            "Invalid email or password.",
            "danger"
        )

    return render_template(
        "auth/login.html",
        form=form
    )

@auth.route("/logout")
@login_required
def logout():
    logout_user()

    flash(
        "You have been logged out successfully.",
        "success"
    )

    return redirect(url_for("auth.login"))