from flask import Flask, render_template, request, redirect, url_for
from lostandfounddatabase import *
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def hello():
    date = request.form.get("date")
    description = request.form.get("description")
    print(date, description)
    print(get_row("3"))
    database_add(date, description)
    return render_template("databasetest.html", outerweardate=[database_display_date()], outerweardescription=[database_display_description()], row1= [get_row("1")], row2= [get_row("2")], row3= [get_row("3")]
    )

#def oneRow():
    return render_template("databasetest.html", row1= [get_row("1")])

def oneDescription(id):
    return render_template(database_display_oneDate(id))


if __name__ == "__main__":
    app.run(debug=True)