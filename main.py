from flask import Flask, make_response, render_template, request, flash, get_flashed_messages, session, redirect, abort, url_for
import cloudinary
from config import token, admin_email, admin_password, secret_key, host, admins
from mongoengine import Document, FileField, ListField, StringField, connect, DateTimeField, IntField, SequenceField, ReferenceField
from mongoengine.context_managers import switch_db
from flask import jsonify
from db import Post_blog, Works_blog
import datetime


mongo = connect(host=host)



app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = secret_key
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['PORT'] = 5000


@app.route('/newwork', methods=['POST'])
def new_work():
    token = request.headers.get('Token')
    if token == admins:
        try:
            data = request.get_json()
            title = data['title']
            description = data['description']
            category = data['category']
            photo_url = data['photo_url']
            post = Works_blog(title = title, content = description, images = [photo_url], category = category, created_at = datetime.datetime.now().year)
            post.save()
            return jsonify({'ok':'yes'}) , 200
        except Exception as ex:
            print(ex)
            abort(400)
    print(token, admins)
    abort(400)

@app.route('/newpost', methods=['POST'])
def new_post():
    print(request.headers)
    token = request.headers.get('Token')
    if token == admins:
        try:
            data = request.get_json()
            title = data['title']
            description = data['description']
            category = data['category']
            photo_url = data['photo_url']
            post = Post_blog(title = title, content = description, images = [photo_url], category = category, created_at = datetime.datetime.now())
            post.save()
            return jsonify({'ok':'yes'}) , 200
        except Exception as ex:
            print(ex)
            abort(400)
    print(token, admins)
    abort(400)

@app.route('/')
def index():
    return render_template('index.html', Post_blog = Post_blog, Works_blog = Works_blog)



if __name__ == '__main__':
    app.run(debug=True)