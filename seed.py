"""Seed db with todo list items."""

from model import ListItem, db, connect_to_db

def add_todo_item(desc):
    """Add item to the todo list."""

    item = ListItem(description=desc)
    db.session.add(item)
    db.session.commit()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

    db.drop_all()
    db.create_all()

    add_todo_item("Walk the dog")
    add_todo_item("Eat chocolate")