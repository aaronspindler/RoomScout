import unittest


def suite():
    return unittest.TestLoader().discover("payments.tests", pattern="*.py")
