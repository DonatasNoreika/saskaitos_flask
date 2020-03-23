import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime
# import forms

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'biudzetas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Zmogus(db.Model):
    __tablename__ = "zmogus"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    asmens_kodas = db.Column("Asmens kodas", db.String)
    tel_numeris = db.Column("Telefono numeris", db.String)

class Bankas(db.Model):
    __tablename__ = "bankas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    adresas = db.Column("Adresas", db.String)
    banko_kodas = db.Column("Banko kodas", db.String)
    swift = db.Column("SWIFT kodas", db.String)

class Saskaita(db.Model):
    __tablename__ = "saskaita"
    id = db.Column(db.Integer, primary_key=True)
    numeris = db.Column("Pavadinimas", db.String)
    zmogus_id = db.Column(db.Integer, db.ForeignKey("zmogus.id"))
    zmogus = db.relationship("Zmogus")
    bankas_id = db.Column(db.Integer, db.ForeignKey("bankas.id"))
    bankas = db.relationship("Zmogus")
    balansas = db.Column("Balansas", db.Float)
