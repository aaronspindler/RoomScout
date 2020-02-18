import unittest


def suite():
	return unittest.TestLoader().discover("security.tests", pattern="*.py")
