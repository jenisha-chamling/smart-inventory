from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import login_required

from . import products
from app.forms import ProductForm
from app.models import Product, Supplier
from app import db


@products.route("/")
@login_required
def product_list():

    products_list = Product.query.order_by(
        Product.id.desc()
    ).all()

    return render_template(
        "products/list.html",
        products=products_list
    )


@products.route("/add", methods=["GET", "POST"])
@login_required
def add_product():

    form = ProductForm()

    suppliers_list = Supplier.query.order_by(
        Supplier.name.asc()
    ).all()

    form.supplier_id.choices = [
        (0, "No Supplier")
    ] + [
        (supplier.id, supplier.name)
        for supplier in suppliers_list
    ]

    if form.validate_on_submit():

        existing_product = Product.query.filter_by(
            sku=form.sku.data
        ).first()

        if existing_product:

            flash(
                "A product with this SKU already exists.",
                "danger"
            )

            return render_template(
                "products/add.html",
                form=form
            )

        product = Product(
            name=form.name.data,
            sku=form.sku.data,
            description=form.description.data,
            quantity=form.quantity.data,
            price=form.price.data,
            reorder_level=form.reorder_level.data,
            supplier_id=(
                form.supplier_id.data
                if form.supplier_id.data != 0
                else None
            )
        )

        db.session.add(product)
        db.session.commit()

        flash(
            "Product added successfully!",
            "success"
        )

        return redirect(
            url_for("products.product_list")
        )

    return render_template(
        "products/add.html",
        form=form
    )


@products.route(
    "/edit/<int:product_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_product(product_id):

    product = Product.query.get_or_404(product_id)

    form = ProductForm(obj=product)

    suppliers_list = Supplier.query.order_by(
        Supplier.name.asc()
    ).all()

    form.supplier_id.choices = [
        (0, "No Supplier")
    ] + [
        (supplier.id, supplier.name)
        for supplier in suppliers_list
    ]

    if request.method == "GET":

        form.supplier_id.data = (
            product.supplier_id
            if product.supplier_id is not None
            else 0
        )

    if form.validate_on_submit():

        existing_product = Product.query.filter(
            Product.sku == form.sku.data,
            Product.id != product.id
        ).first()

        if existing_product:

            flash(
                "Another product already uses this SKU.",
                "danger"
            )

            return render_template(
                "products/edit.html",
                form=form,
                product=product
            )

        product.name = form.name.data
        product.sku = form.sku.data
        product.description = form.description.data
        product.quantity = form.quantity.data
        product.price = form.price.data
        product.reorder_level = form.reorder_level.data

        product.supplier_id = (
            form.supplier_id.data
            if form.supplier_id.data != 0
            else None
        )

        db.session.commit()

        flash(
            "Product updated successfully!",
            "success"
        )

        return redirect(
            url_for("products.product_list")
        )

    return render_template(
        "products/edit.html",
        form=form,
        product=product
    )


@products.route(
    "/delete/<int:product_id>",
    methods=["POST"]
)
@login_required
def delete_product(product_id):

    product = Product.query.get_or_404(product_id)

    db.session.delete(product)
    db.session.commit()

    flash(
        "Product deleted successfully.",
        "success"
    )

    return redirect(
        url_for("products.product_list")
    )