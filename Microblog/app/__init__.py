#!/usr/venv python3
""" Make a package the directory"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
