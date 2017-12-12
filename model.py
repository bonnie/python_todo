"""Database Model for todo app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ListItem(db.Model):
    """Item in the todo list."""

    __tablename__ = 'list_items'

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    description = db.Column(db.Text, nullable=False)


def connect_to_db(app, db_uri='postgresql:///python_todo'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == '__main__':

    from server import app

    connect_to_db(app)
    # db.drop_all()
    # db.create_all()

    print("connected to DB")