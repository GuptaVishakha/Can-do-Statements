from atexit import register
from imghdr import tests
from flask import redirect, render_template, request, Blueprint, flash, url_for, session
from project.general.models import Users, Tests, TestResults
from datetime import datetime
from project.forms import forms

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if session.get("HawkID"):
        return redirect(url_for("auth.dashboard"))
    else:
        if request.method == "POST":
            HawkID = request.form.get("HawkID")
            user = Users.query.filter_by(HawkID=HawkID).first()
            if user:
                flash("Login successful")
                session["HawkID"] = user.HawkID
                return redirect(url_for("auth.dashboard"))
            else:
                flash(
                    "User not found - Please check your HawkID or Register as new user"
                )
                return render_template("login.html")

        else:
            return render_template("login.html")


@auth.route("/dashboard")
def dashboard():
    if session.get("HawkID"):
        HawkID = session.get("HawkID")
        # user = Users.query.filter_by(HawkID=HawkID).first()
        tests = Tests.query.all()
        render_data = []
        # tests = [r.__dict__ for r in tests]
        for t in tests:
            data = {
                "HawkID": HawkID,
                "TestID": str(t.id),
                "Level": t.TestLevel,
                "Name": t.Name,
                "URL": t.URL,
                "Description": t.Description,
                "Score": None,
                "Date": None,
            }
            score = (
                TestResults.query.order_by(TestResults.TestDate.desc())
                .filter_by(HawkID=HawkID, TestID=t.id)
                .first()
            )
            if score:
                data["Score"] = score.Result
                data["Date"] = score.TestDate

            render_data.append(data)

        return render_template("dashboard.html", render_data=render_data)

    else:
        flash("Please Login")
        return redirect(url_for("auth.login"))
