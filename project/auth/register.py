from atexit import register
from codecs import register_error
import re
from flask import redirect, render_template, request, Blueprint, flash, url_for, session
from project.general.models import Users
from project.models import db

register = Blueprint(
    "register",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@register.route("/register", methods=("GET", "POST"))
def registration():
    if request.method == "POST":

        if session.get("HawkID"):
            session.pop("HawkID")

        form = request.form

        HawkID = request.form.get("HawkID")
        FirstName = request.form.get("FirstName")
        MiddleName = request.form.get("MiddleName")
        LastName = request.form.get("LastName")
        Department = request.form.get("Department")
        Course = request.form.get("Course")
        Role = request.form.get("Role")

        required_fields = [
            HawkID,
            FirstName,
            MiddleName,
            LastName,
            Department,
            Course,
            Role,
        ]

        if "" in required_fields:
            flash("You are missing one or more required fields")
            return render_template("register.html")

        if Users.query.filter_by(HawkID=HawkID).first():
            flash("HawkID already exists, please login")
            return render_template("register.html")

        user = Users(HawkID, FirstName, LastName, Department, Course)
        user.set_user_role(Role)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful")
        return redirect(url_for("auth.login"))

    else:
        return render_template("register.html")
