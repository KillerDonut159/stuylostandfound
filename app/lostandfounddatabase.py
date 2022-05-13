from flask import Flask, render_template, request, redirect, url_for
from sqlite3 import connect, Row
from os import system

def create_database():
    open("lost_and_found.db", "w")
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("create table outerwear (date text, description text)")
    c.execute("insert into outerwear values ('5/12/22', 'Heheheha')")
    db.commit()
    db.close()

def database_add(date, description):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("insert into outerwear values (?, ?)", (date, description))
    db.commit()
    db.close() 

def database_display():
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select * from outerwear;")
    result = list(c.fetchall())
    db.close()
    return result

create_database()