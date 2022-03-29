from sqlite3 import connect, Row


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

def row_to_dic(row):
    dic = dict(row)
    dic.pop("found")
    dic.pop("category")
    return dic

def get_items(category):
    db = connect("data.db")
    c = db.cursor()
    c.row_factory = Row
    c.execute("SELECT * FROM mesa WHERE category = ? AND found = 0", (category,))
    result = list(map(row_to_dic, c.fetchall()))
    db.close()
    return result

def update_found(id, found):
    db = connect("data.db")
    c = db.cursor()
    if found:
        found = 1
    else:
        found = 0
    c.execute("UPDATE mesa SET found = ? WHERE id = ?", (found, id))
    db.commit()
    db.close()
