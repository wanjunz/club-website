from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session

# Importing quote function to handle URL encoding
from urllib.parse import quote 

#library for database management
import sqlite3

app = Flask(__name__)

# Configure session 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def default():
    return render_template('index.html')