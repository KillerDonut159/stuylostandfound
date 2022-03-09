from sqlite3 import connect

TABLES = ["outwear", "gloves", "schoolsupplies", "books", "smallitems"]
FIELDS = ["number", "date", "description", "link"]

def mapa(function, *lsts):
    return list(map(function, *lsts))

def add_type(field):
    return f"{field} TEXT"

def get_question_mark(field):
    return "?"

def get_list_string(strings):
    return f"({', '.join(strings)})"

def first(lst):
    return lst[0]

def get_item(*values):
    return dict(zip(FIELDS, values))

def reset_data():
    open("data.db", "w").close()
    db = connect("data.db")
    c = db.cursor()
    for table in TABLES:
        c.execute(f"CREATE TABLE IF NOT EXISTS {table} {get_list_string(mapa(add_type, FIELDS))}")
    db.commit()

def add_item(table, item):
    db = connect("data.db")
    c = db.cursor()
    c.execute(f"INSERT INTO {table} VALUES {get_list_string(map(get_question_mark, FIELDS))}", mapa(item.get, FIELDS))
    db.commit()

def get_column(table, field):
    db = connect("data.db")
    c = db.cursor()
    c.execute(f"SELECT {field} from {table}")
    return mapa(first, c.fetchall())

def get_items(table):
    def get_table_column(field):
        return get_column(table, field)
    columns = mapa(get_table_column, FIELDS)
    def get_table_item(*values):
        return dict(zip(FIELDS, values))
    return mapa(get_table_item, *columns)
