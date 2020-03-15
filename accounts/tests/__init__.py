import unittest


def suite():
    return unittest.TestLoader().discover("accounts.tests", pattern="*.py")
