from flask import Flask, make_response, render_template, request, flash, get_flashed_messages, session, redirect, abort, url_for
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from config import token, admin_email, admin_password, secret_key, host
from mongoengine import Document, FileField, ListField, StringField, connect, DateTimeField, IntField, SequenceField, ReferenceField
from mongoengine.context_managers import switch_db
from flask import jsonify
from concurrent.futures import ProcessPoolExecutor
from threading import Thread
from werkzeug.serving import run_simple
from multiprocessing import Process
import os
mongo = connect(host=host)

def verify_email(email):
    if email == admin_email:
        return True
    return False


def verify_password(password):
    if password == admin_password:
        return True
    return False




app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = secret_key
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['PORT'] = 5000

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)