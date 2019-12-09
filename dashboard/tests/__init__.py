import unittest


def suite():
	return unittest.TestLoader().discover("dashboard.tests", pattern="*.py")
