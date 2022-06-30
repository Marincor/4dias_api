
from flask import Blueprint, make_response, render_template


main = Blueprint('main', __name__);

@main.route("", methods=["GET"])
def welcome():
    return make_response(render_template("index.html")), 200