from sqlite3 import connect

DB_NAME = "data.db"
DB = connect(DB_NAME)
C = DB.cursor()
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
    open(DB_NAME, "w").close()
    for table in TABLES:
        C.execute(f"CREATE TABLE IF NOT EXISTS {table} {TABLE_HEADER}")
    DB.commit()

def add_item(table, item):
    C.execute(f"INSERT INTO {table} VALUES {BLANK_TABLE_ROW}", mapa(item.get, FIELDS))
    DB.commit()

def get_column(table, field):
    C.execute(f"SELECT {field} FROM {table}")
    return mapa(first, C.fetchall())

def first(lst):
    return lst[0]

def get_items(table):
    def get_table_column(field):
        return get_column(table, field)
    columns = mapa(get_table_column, FIELDS)
    return mapa(get_item, *columns)
