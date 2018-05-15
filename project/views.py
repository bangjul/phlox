import os, json

from flask import Flask, request, Response, jsonify, json
from flask import render_template, url_for, redirect, send_from_directory
from flask import make_response, abort, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


# Web Profile
@app.route('/')
def index():
    return render_template('index.php', title="julioTA")