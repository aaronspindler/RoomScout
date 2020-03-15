import unittest


def suite():
    return unittest.TestLoader().discover("emails.tests", pattern="*.py")
