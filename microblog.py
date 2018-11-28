# -*- coding: utf-8 -*-
__author__ = 'Terence Jie'
__time__ = '2018/11/15 16:14'
from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
