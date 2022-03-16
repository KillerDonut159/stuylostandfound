from time import time
from datetime import date

def get_date():
    return date.fromtimestamp(time()).strftime("%-m/%-d/%y")
