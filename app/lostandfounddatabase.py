from flask import Flask, render_template, request, redirect, url_for
from sqlite3 import connect, Row
from os import system

def create_database():
    open("lost_and_found.db", "w")
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("create table lost (id INTEGER PRIMARY KEY, type text, date text, description text, image1 text, image2 text)")
    db.commit()
    db.close()

def database_add(type, date, description, image1, image2):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("insert into lost (type, date, description, image1, image2) values (?, ?, ?, ?, ?)", (type, date, description, image1, image2))
    db.commit()
    db.close() 

def database_delete(idnum):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("delete from lost where ROWID = (?);", (idnum))
    db.commit()
    db.close() 

def database_display_all(type):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select date, description, image1, image2 from lost WHERE type = ?;", (type,))
    result = list(c.fetchall())
    db.close()
    return result

def database_display_full():
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select * from lost;")
    result = list(c.fetchall())
    db.close()
    return result

def database_display_date():
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select date from lost;")
    result = list(c.fetchall())
    db.close()
    return result

def database_display_description():
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select description from lost;")
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

#def get_row(idnum):
    db = connect("lost_and_found.db")
    c = db.cursor()
    c.execute("select date, description from lost where ROWID = (?);", (idnum))
    result = list(c.fetchall())
    db.close()
    return result

#print(get_row("2"))
