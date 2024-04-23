from flask import Blueprint
from flask import render_template, redirect, url_for
from flask.views import View

from source.front.smkg_base import BaseView

smkg_index = Blueprint("index", __name__, url_prefix="/index", template_folder="templates")


class SMKGIndex(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        return render_template("index.html")


smkg_index.add_url_rule("/", view_func=SMKGIndex.as_view("index"))
