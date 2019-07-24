import unittest


def suite():
	return unittest.TestLoader().discover("utils.tests", pattern="*.py")
