import os
from miniblog import create_app, db
import unittest
import tempfile
from miniblog.scripts.db import InitDB, DropDB

class TestMiniBlog(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.app = create_app({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///{}'.format(self.db_path)
        })
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        InitDB().run()

    def tearDown(self):
        DropDB().run()
        self.app_context.pop()
        os.unlink(self.db_path)

    def login(self, username, password):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('shige', 'kano88')
        assert 'ログインしました'.encode() in rv.data
        rv = self.logout()
        assert 'ログアウトしました'.encode() in rv.data
        rv = self.login('admin', 'kano88')
        assert 'ユーザ名が異なります'.encode() in rv.data
        rv = self.login('shige', 'kanokanokano')
        assert 'パスワードが異なります'.encode() in rv.data

if __name__ == '__main__':
    unittest.main()
