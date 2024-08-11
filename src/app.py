from flask import Blueprint, request, jsonify, render_template
from . import db
from .models import Message
from .spam_filter import is_spam

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        content = request.json['content']
        spam = is_spam(content)
        message = Message(content=content, spam=spam)
        db.session.add(message)
        db.session.commit()
        return jsonify({"id": message.id, "content": content, "spam": spam})
    elif request.method == 'GET':
        messages = Message.query.all()
        return jsonify([{"id": m.id, "content": m.content, "spam": m.spam} for m in messages])

if __name__ == '__main__':
    from . import create_app
    app = create_app()
    app.run(debug=True)