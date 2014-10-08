import unittest
from mock import MagicMock, patch
from login import login

class login_test(unittest.TestCase):
    def setUp(self):
        self.loginclass = login()

    def test_successful_login(self):
        pass

    @patch('login.login.get_user')
    def test_correct_type_on_login(self, mock_get_user):
        user = MagicMock()
        user.uname = "manager"
        user.passhash = "$2a$12$CyLyLDPA5NFTY48o3fANQOEsni38JgHBk3FNwdUFd1OwYMBZxN146"
        user.utype = "manager"
        mock_get_user.return_value = user
        utype = self.loginclass.login_user("manager", "password")
        self.assertEqual(utype, "manager")

    def test_unsuccessful_login(self):
        utype = self.loginclass.login_user("manager", "password")
        self.assertEqual(utype, None)
