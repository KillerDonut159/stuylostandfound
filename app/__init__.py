from flask import Flask, render_template, request, redirect, url_for
from lostandfounddatabase import *
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def hello():
    date = request.form.get("date")
    description = request.form.get("description")
    #print(date, description)
    #print(get_row("3"))
    database_add(date, description)
    return render_template(
        "databasetest.html", 
        outerweardisplay=[database_display_all()], 
        outerweardate=[database_display_date()], 
        outerweardescription=[database_display_description()], 
        rows=database_display_all()
    )

if __name__ == "__main__":
    app.run(debug=True)