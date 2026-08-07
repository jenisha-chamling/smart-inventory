from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from . import suppliers
from app.forms import SupplierForm
from app.models import Supplier
from app import db


@suppliers.route("/")
@login_required
def supplier_list():

    suppliers_list = Supplier.query.order_by(
        Supplier.id.desc()
    ).all()

    return render_template(
        "suppliers/list.html",
        suppliers=suppliers_list
    )


@suppliers.route("/add", methods=["GET", "POST"])
@login_required
def add_supplier():

    form = SupplierForm()

    if form.validate_on_submit():

        supplier = Supplier(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            contact_person=form.contact_person.data
        )

        db.session.add(supplier)
        db.session.commit()

        flash(
            "Supplier added successfully!",
            "success"
        )

        return redirect(
            url_for("suppliers.supplier_list")
        )

    return render_template(
        "suppliers/add.html",
        form=form
    )


@suppliers.route(
    "/edit/<int:supplier_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_supplier(supplier_id):

    supplier = Supplier.query.get_or_404(supplier_id)

    form = SupplierForm(obj=supplier)

    if form.validate_on_submit():

        supplier.name = form.name.data
        supplier.email = form.email.data
        supplier.phone = form.phone.data
        supplier.address = form.address.data
        supplier.contact_person = form.contact_person.data

        db.session.commit()

        flash(
            "Supplier updated successfully!",
            "success"
        )

        return redirect(
            url_for("suppliers.supplier_list")
        )

    return render_template(
        "suppliers/edit.html",
        form=form,
        supplier=supplier
    )


@suppliers.route(
    "/delete/<int:supplier_id>",
    methods=["POST"]
)
@login_required
def delete_supplier(supplier_id):

    supplier = Supplier.query.get_or_404(supplier_id)

    db.session.delete(supplier)
    db.session.commit()

    flash(
        "Supplier deleted successfully.",
        "success"
    )

    return redirect(
        url_for("suppliers.supplier_list")
    )