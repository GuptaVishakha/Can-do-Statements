from datetime import datetime
from enum import unique
from tkinter.tix import Tree
from project.models import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    HawkID = db.Column(db.String(10), unique=True)
    FirstName = db.Column(db.String(200), nullable=False)
    MiddleName = db.Column(db.String(200), default="")
    LastName = db.Column(db.String(200), nullable=False)
    Department = db.Column(db.String(100), nullable=False)
    Course = db.Column(db.String(100))
    Role = db.Column(db.String(20), nullable=False, default="student")

    def __init__(
        self,
        HawkID,
        FirstName,
        LastName,
        Department,
        Course,
        MiddleName=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.HawkID = HawkID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Department = Department
        self.Course = Course
        if MiddleName is not None:
            self.MiddleName = MiddleName

    def __repr__(self):
        return f"HawkID: {self.HawkID}"

    def set_user_role(self, role):
        assert type(role) == str
        role = role.lower()
        if role in ("student", "instructor", "admin"):
            self.role = role


class Tests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True, nullable=False)
    TestLevel = db.Column(db.Integer, nullable=False)
    Description = db.Column(db.String(100))
    URL = db.Column(db.String(100))

    def __init__(self, Name, TestLevel, Description, URL, **kwargs):
        super().__init__(**kwargs)
        self.Name = Name
        self.TestLevel = TestLevel
        self.Description = Description
        self.URL = URL


class TestResults(db.Model):
    TestDate = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        primary_key=True,
        autoincrement=False,
    )
    Result = db.Column(db.String(100), primary_key=True, autoincrement=False)
    HawkID = db.Column(db.String(10), db.ForeignKey("users.HawkID"), nullable=False)
    user = db.relationship("Users", backref=db.backref("TestResults", lazy=True))
    TestID = db.Column(db.Integer, db.ForeignKey("tests.id"), nullable=False)
    test = db.relationship("Tests", backref=db.backref("TestResults", lazy=True))

    _mapper_args__ = {
        "order_by": TestDate,
    }

    def __init__(self, HawkID, TestID, Result, **kwargs):
        super().__init__(**kwargs)
        self.HawkID = HawkID
        self.TestDate = datetime.now()
        self.TestID = TestID
        self.Result = Result
