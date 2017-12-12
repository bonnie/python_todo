"""Flask app for example Python todo list."""

from flask import Flask, request
from model import ListItem

app = Flask(__name__)

@app.route('/')
def show_items():
    """Show index table of todo list items."""

    items = ListItem.query.all()
    return render_template('todo.html', items=items)

if __name__ == '__main__':
    app.run()