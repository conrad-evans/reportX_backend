from sys import setdlopenflags
from src.db import DataBase


class Test_Database:
    db = DataBase()

    def test_init(self):
        # assert
        assert type(self.db.db) is dict
        assert self.db.db == dict()

    def test_userInDB(self):
        pass

    def test_saveUser(self):
        user = {
            'email': 'test@mail.com',
            'password': '12345678'
        }
        self.db.saveUser(user)
        assert len(self.db.db) == 1

    def test_generateRandomId(self):
        id = self.db.generateRandomId()
        assert type(id) == str

    def test_checkUserId(self):
        pass

    def test_saveRedFlag(self):
        pass

    def test_getUserReadFlags(self):
        pass

    def test_getAllRedFlags(self):
        pass

    def test_getRedFlag(self):
        pass

    def test_getARedFlag(self):
        pass

    def test_editRedFlag(self):
        pass

    def test_deleteRedFlag(self):
        pass
