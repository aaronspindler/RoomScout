import unittest


def suite():
    return unittest.TestLoader().discover("houses.tests", pattern="*.py")
