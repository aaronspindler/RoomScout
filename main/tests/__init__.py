import unittest


def suite():
    return unittest.TestLoader().discover("main.tests", pattern="*.py")
