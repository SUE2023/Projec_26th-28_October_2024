#!/usr/venv python3
""" Make a package the directory"""
from flask import Flask

app = Flask(__name__)

from app import routes
