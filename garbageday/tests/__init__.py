import unittest


def suite():
    return unittest.TestLoader().discover("garbageday.tests", pattern="*.py")
