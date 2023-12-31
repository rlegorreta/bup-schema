from flask import Flask
import logging

app = Flask(__name__)
app.config["INFO"] = True
logging.getLogger().setLevel(logging.INFO)

from app import controller
from app import neo4jdb
from app import schema