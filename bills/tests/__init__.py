import unittest


def suite():
    return unittest.TestLoader().discover("bills.tests", pattern="*.py")
