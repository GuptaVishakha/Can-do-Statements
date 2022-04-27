from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect, session
from project.general.models import Users

general = Blueprint(
    "general",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/assets",
)


@general.route("/", methods=["POST", "GET"])
def home():
    if session.get("HawkID"):
        HawkID = session.get("HawkID")
        user = Users.query.filter_by(HawkID=HawkID).first()
        return render_template("home.html", username=user.FirstName)

    return render_template("home.html")
