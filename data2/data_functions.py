from sqlite3 import connect


def reset_data():
    open("data.db", "w").close()
    db = connect("data.db")
    c = db.cursor()
    c.execute("CREATE TABLE mesa (id INTEGER, found INTEGER, category TEXT, date TEXT, description TEXT, link TEXT)")
    db.commit()
    db.close()

def get_next_id():
    db = connect("data.db")
    c = db.cursor()
    c.execute("SELECT MAX(id) FROM mesa")
    max_id = c.fetchone()[0]
    db.close()
    if max_id == None:
        return 0
    return max_id + 1

def add_item(category, date, description, link):
    db = connect("data.db")
    c = db.cursor()
    c.execute("INSERT INTO mesa VALUES (?, ?, ?, ?, ?, ?)", (get_next_id(), 0, category, date, description, link))
    db.commit()
    db.close()
