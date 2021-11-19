from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Cupcake

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql"="///cupcakes_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True
app.config['SECRET_KEY']="secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

debug=DebugToolbarExtension(app)

connect_db(app)
