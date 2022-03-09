from sqlite3 import connect

TABLES = ["outwear", "gloves", "schoolsupplies", "books", "smallitems"]
FIELDS = ["number", "date", "description", "link"]

def mapa(function, *lsts):
    return list(map(function, *lsts))

def get_list_string(strings):
    return f"({', '.join(strings)})"

def add_type(field):
    return f"{field} TEXT"

def get_question_mark(field):
    return "?"

TABLE_HEADER = get_list_string(mapa(add_type, FIELDS))
BLANK_TABLE_ROW = get_list_string(mapa(get_question_mark, FIELDS))

def get_item(*values):
    return dict(zip(FIELDS, values))

def reset_data():
    open("data.db", "w").close()
    db = connect("data.db")
    c = db.cursor()
    for table in TABLES:
        c.execute(f"CREATE TABLE IF NOT EXISTS {table} {TABLE_HEADER}")
    db.commit()

def add_item(table, item):
    db = connect("data.db")
    c = db.cursor()
    c.execute(f"INSERT INTO {table} VALUES {BLANK_TABLE_ROW}", mapa(item.get, FIELDS))
    db.commit()

def get_column(table, field):
    db = connect("data.db")
    c = db.cursor()
    c.execute(f"SELECT {field} FROM {table}")
    return mapa(first, c.fetchall())

def first(lst):
    return lst[0]

def get_items(table):
    def get_table_column(field):
        return get_column(table, field)
    columns = mapa(get_table_column, FIELDS)
    return mapa(get_item, *columns)
