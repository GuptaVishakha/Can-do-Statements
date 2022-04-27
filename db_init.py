import os
from app import create_app
from project.general.models import Users, TestResults, Tests

app = create_app()

tests = {
    "NoviceLow": {
        "Level": 1,
        "Description": "Novice Low Can-Do Statements",
        "URL": "Novice Low Can-Do Statements.html",
    },
    "NoviceMid": {
        "Level": 2,
        "Description": "Novice Mid Can-Do Statements",
        "URL": "Novice Mid Can-Do Statements.html",
    },
    "NoviceHigh": {
        "Level": 3,
        "Description": "Novice High Can-Do Statements",
        "URL": "Novice High Can-Do Statements.html",
    },
    "IntermediateLow": {
        "Level": 4,
        "Description": "Intermediate Low Can-Do Statements",
        "URL": "Intermediate Low Can-Do Statements.html",
    },
    "IntermediateMid": {
        "Level": 5,
        "Description": "Intermediate Mid Can-Do Statements",
        "URL": "Intermediate Mid Can-Do Statements.html",
    },
    "IntermediateHigh": {
        "Level": 6,
        "Description": "Intermediate High Can-Do Statements",
        "URL": "Intermediate High Can-Do Statements.html",
    },
    "AdvancedLow": {
        "Level": 7,
        "Description": "Advanced Low Can-Do Statements",
        "URL": "Advanced Low Can-Do Statements.html",
    },
    "AdvancedMid": {
        "Level": 8,
        "Description": "Advanced Mid Can-Do Statements",
        "URL": "Advanced Mid Can-Do Statements.html",
    },
    "AdvancedHigh": {
        "Level": 9,
        "Description": "Advanced High Can-Do Statements",
        "URL": "Advanced High Can-Do Statements.html",
    },
}


def seed(db):
    user = Users("admin", "admin", "admin", "admin", "admin")
    user.set_user_role("admin")
    db.session.add(user)
    db.session.commit()
    user = Users("01342267", "Vishakha", "Gupta", "Computer Science", "French")
    user.set_user_role("instructor")
    db.session.add(user)
    db.session.commit()
    user = Users("01311142", "Tanay", "Chougule", "Engineering", "French")
    user.set_user_role("student")
    db.session.add(user)
    db.session.commit()
    for key, val in tests.items():

        test = Tests(key, val["Level"], val["Description"], val["URL"])
        db.session.add(test)
        db.session.commit()


with app.app_context():

    from project.models import db
    from project.general.models import Users, TestResults

    db.drop_all()

    db.create_all()
    seed(db)
