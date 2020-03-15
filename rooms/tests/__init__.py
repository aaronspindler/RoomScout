import unittest


def suite():
    return unittest.TestLoader().discover("rooms.tests", pattern="*.py")
