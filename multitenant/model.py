# -*- coding: utf-8 -*-

from .core import db


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())