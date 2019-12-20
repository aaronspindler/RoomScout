def test_FUNCTION_get(self):
	print('Testing FUNCTION() GET')
	self.client.force_login(self.user)


def test_FUNCTION_get_not_logged_in(self):
	print('Testing FUNCTION() GET not logged in')
	self.client.logout()


def test_FUNCTION_get_wrong_user(self):
	print('Testing FUNCTION() GET wrong user')
	self.client.force_login(self.user2)


def test_FUNCTION_post(self):
	print('Testing FUNCTION() POST')
	self.client.force_login(self.user)


def test_FUNCTION_post_not_logged_in(self):
	print('Testing FUNCTION() POST not logged in')
	self.client.logout()


def test_FUNCTION_post_wrong_user(self):
	print('Testing FUNCTION() POST wrong user}')
	self.client.force_login(self.user2)