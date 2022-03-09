from sqlite3 import connect

DB_NAME = "data.db"
TABLES = ["outwear", "gloves", "schoolsupplies", "books", "smallitems"]
FIELDS = ["number", "date", "description", "link"]

def mapa(function, *lsts):
    return list(map(function, *lsts))

def get_field_string(function):
    return f"({', '.join(mapa(function, FIELDS))})"

def add_type(field):
    return f"{field} TEXT"

def get_question_mark(field):
    return "?"

DB = connect(DB_NAME)
C = DB.cursor()
TABLE_HEADER = get_field_string(add_type)
BLANK_TABLE_ROW = get_field_string(get_question_mark)

def get_item(*values):
    return dict(zip(FIELDS, values))

def reset_data():
    open(DB_NAME, "w").close()
    for table in TABLES:
        C.execute(f"CREATE TABLE IF NOT EXISTS {table} {TABLE_HEADER}")
    DB.commit()

def add_item(table, item):
    C.execute(f"INSERT INTO {table} VALUES {BLANK_TABLE_ROW}", mapa(item.get, FIELDS))
    DB.commit()

def first(lst):
    return lst[0]

def get_column(table, field):
    C.execute(f"SELECT {field} FROM {table}")
    return mapa(first, C.fetchall())

def get_items(table):
    def get_table_column(field):
        return get_column(table, field)
    return mapa(get_item, *mapa(get_table_column, FIELDS))
