# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2018/11/28 18:01'

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes