from flask import Flask, render_template, request, redirect, url_for
from sqlite3 import connect, Row
from os import system

def create_database():
    open("lost_and_found.db", "w")
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("create table outerwear (INTEGER PRIMARY KEY, date text, description text)")
    db.commit()
    db.close()

def database_add(date, description):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("insert into outerwear(date, description) values (?, ?)", (date, description))
    db.commit()
    db.close() 

def database_display_date():
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select date from outerwear;")
    result = list(c.fetchall())
    db.close()
    return result

def database_display_description():
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select description from outerwear;")
    result = list(c.fetchall())
    db.close()
    return result

#def database_display_oneDate(id):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select date from outerwear where ROWID= (?);", (id))
    result = list(c.fetchall())
    db.close()
    return result

#def database_display_oneDescription(id):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select description from outerwear where rowid = (?);", (id))
    result = list(c.fetchall())
    db.close()
    return result

def get_row(idnum):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select * from outerwear where ROWID = (?);", (idnum))
    result = list(c.fetchall())
    db.close()
    return result

create_database()
print(get_row("2"))
