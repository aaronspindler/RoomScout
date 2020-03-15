import datetime
import re

"""
    Input is supposed to be in the format yyyy-mm-dd
    if it is not then return false
"""


def check_format(input):
    if isinstance(input, datetime.date):
        return True
    else:
        return bool(re.match(r"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", input))
