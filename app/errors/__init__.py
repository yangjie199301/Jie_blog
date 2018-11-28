# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2018/11/28 15:39'

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers