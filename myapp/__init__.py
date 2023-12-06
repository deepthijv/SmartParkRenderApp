import os

from flask import Flask 

from .extensions import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://smartpark_user_db_user:93k5SkAxyRqiZ7l6hHxXydPrFSLpMIrn@dpg-clo2h0n5felc73a1ca5g-a/smartpark_user_db"
    # postgres://prettyprinted_render_example_user:11vq6k72GmFJazhVpz3pFUko50djVZT1@dpg-ceukdhmn6mpglqdb4avg-a.oregon-postgres.render.com/prettyprinted_render_example

    db.init_app(app)

    app.register_blueprint(main)

    return app