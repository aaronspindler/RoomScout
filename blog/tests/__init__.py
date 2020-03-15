import unittest


def suite():
    return unittest.TestLoader().discover("blog.tests", pattern="*.py")
