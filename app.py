from flask import Flask, session
import os


def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/cando"
    # app.config["SQLALCHEMY_DATABASE_URI"] = (
    #     "mysql://dev:voter_portal#" "@localhost/can_do"
    # )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
    app.config["SECRET_KEY"] = str(os.urandom(12).hex())

    from project.models import db

    db.init_app(app)

    from project.general.models import Users, TestResults

    from project.general.general import general
    from project.forms.forms import forms
    from project.auth.auth import auth
    from project.auth.register import register

    app.register_blueprint(general)
    app.register_blueprint(forms)
    app.register_blueprint(auth)
    app.register_blueprint(register)

    return app


app = create_app()
app.run(debug=True)
