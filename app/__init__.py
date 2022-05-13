from flask import Flask, render_template, request, redirect, url_for
import lostandfounddatabase
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello():
    date = request.form.get("date")
    description = request.form.get("description")
    print(date, description)
    lostandfounddatabase.database_add(date, description)
    return render_template("databasetest.html", outerweartable=[lostandfounddatabase.database_display()
    ])

if __name__ == "__main__":
    app.run(debug=True)