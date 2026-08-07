from flask import Blueprint

suppliers = Blueprint(
    "suppliers",
    __name__,
    url_prefix="/suppliers"
)

from . import routes