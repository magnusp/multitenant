# -*- coding: utf-8 -*-

from flask import Flask
from .core import db


def create_app(package_name, settings_override=None):
    app = Flask(package_name)

    app.config.from_object('multitenant.settings')
    app.config.from_envvar('FLASK_SETTINGS', silent=True)
    app.config.from_object(settings_override)

    db.init_app(app)

    return app