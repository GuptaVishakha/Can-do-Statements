from flask import Blueprint, session
from flask import redirect, render_template, request, Blueprint, flash, url_for
from project.general.models import Users, Tests, TestResults
from project.models import db

forms = Blueprint(
    "forms",
    __name__,
    template_folder="templates",
    static_folder="static",
)


def getFormScore(form, key="inp-checkbox-response"):
    return len(form.getlist(key))


@forms.route("/forms/<int:TestID>", methods=["GET", "POST"])
def getFormbyID(TestID):
    test = Tests.query.filter_by(id=TestID).first_or_404()
    if session.get("HawkID"):
        hawkID = session.get("HawkID")
        if request.method == "POST":
            curr_score = getFormScore(request.form)
            result = TestResults(hawkID, TestID, curr_score)
            db.session.add(result)
            db.session.commit()
            return redirect(
                url_for(
                    "auth.dashboard",
                )
            )
        else:
            return render_template(test.URL)
    else:
        flash("Please Login")
        return redirect(url_for("auth.login"))


@forms.route("/forms/<TestName>", methods=["GET", "POST"])
def getFormbyName(TestName):
    test = Tests.query.filter_by(Name=TestName).first_or_404()
    hawkID = session.get("HawkID")
    if request.method == "POST":
        curr_score = getFormScore(request.form)
        result = TestResults(hawkID, test.id, curr_score)
        db.session.add(result)
        db.session.commit()
        return redirect(
            url_for(
                "auth.dashboard",
            )
        )
    else:
        return render_template(test.URL)
