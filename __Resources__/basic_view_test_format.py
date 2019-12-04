def test_FUNCTION_get(self):
	self.client.force_login(self.user)


def test_FUNCTION_get_not_logged_in(self):
	self.client.logout()


def test_FUNCTION_get_wrong_user(self):
	self.client.force_login(self.user2)


def test_FUNCTION_post(self):
	self.client.force_login(self.user)


def test_FUNCTION_post_not_logged_in(self):
	self.client.logout()


def test_FUNCTION_post_wrong_user(self):
	self.client.force_login(self.user2)