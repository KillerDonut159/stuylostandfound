from flask import Flask, render_template, request, redirect, url_for
import base64
#import io
#import whatimage
#import pyheif
#from PIL import Image
from lostandfounddatabase import *
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello():
    return render_template(
        "databasetest.html", 
        bookspapers=database_display_all('bookspapers'),
        outerwear=database_display_all('outerwear'),
        gloves=database_display_all('gloveshatsscarves'),
        personalschool=database_display_all('personalschoolsupplies'),
        smallitems=database_display_all('smallitems'),
        full=database_display_full(),
    )

@app.route("/", methods=["GET","POST"])
def itsme():
    return render_template(
        "bookspapers.html", 
        bookspapers=database_display_all('bookspapers')
    )

@app.route("/", methods=["GET","POST"])
def iwaswondering():
    return render_template(
        "outerwear.html", 
        outerwear=database_display_all('outerwear')
    )

@app.route("/", methods=["GET","POST"])
def ifafteralltheseyears():
    return render_template(
        "gloves.html", 
        gloves=database_display_all('gloveshatsscarves')
    )

@app.route("/", methods=["GET","POST"])
def youdliketomeet():
    return render_template(
        "personalschoolsupplies.html", 
        personalschool=database_display_all('personalschoolsupplies')
    )

@app.route("/", methods=["GET","POST"])
def togoovereverything():
    return render_template(
        "smallitems.html", 
        smallitems=database_display_all('smallitems')
    )

@app.route("/submit", methods=["POST"])
def submit():
    type = request.form.get("type")
    date = request.form.get("date")
    description = request.form.get("description")
    images = [None, None]
    image_names = ['image1', 'image2']
    for index, image_name in enumerate(image_names):
        if image_name in request.files:
            image = request.files[image_name].read()

            #Attempt to add a HEIC to JPEG converter
            """fmt = whatimage.identify_image(image)
            if fmt in ['heic', 'avif']:
                i = pyheif.read_heif(image)
                # Convert to other file format like jpeg
                s = io.BytesIO()
                image = Image.frombytes(
                    mode=i.mode, size=i.size, data=i.data)

                image.save(s, format="jpeg")
                image = image.read()"""

            image_string = base64.b64encode(image)
            images[index] = image_string.decode('utf-8')

    database_add(type, date, description, images[0], images[1])
    return redirect(url_for('hello'))

@app.route("/confirm", methods=["GET","POST"])
def delete():
    idnum = request.form.get("idn")
    database_delete(idnum)
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=True)