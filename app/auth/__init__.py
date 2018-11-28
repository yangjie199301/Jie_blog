# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2018/11/28 17:18'
from flask import Blueprint

bp = Blueprint('auth',__name__)

from app.auth import routes