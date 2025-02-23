from datetime import datetime

from src.dd_tmgbedu.dd import dd, dump


class Permission:
    def __init__(self, name):
        self.name = name


class Role:
    def __init__(self, role):
        self.permission = Permission(role)


class User:
    classy = 1
    example = None,
    dict = {}
    dob = None

    @property
    def dyno(self):
        return 1

    def __init__(self):
        self.stasis = 2
        self._password = 'password'
        self.__token = 'token'
        self.role = Role('admin')
        self.dob = datetime.now()

    def fx(self):
        return 3


dump("Hello Python")
dump('')
dump({})

dump(1)
dump(1.123)
dump(['hello', 'hi', 'ok'])
dump(['apple', ['banana', 1, 3, 'cat'], 'ok'])
dump([1, 2, 3, 4])
dump(("mouse", [8, 4, 6], (1, 2, 3)))
dump({
    "apple": "banana",
    "banana": "cherry",
    "cherry": "apple",
    'dog': {
        'color': 'green',
        'size': 'large',
        'category': {
            'apple': 'apple',
            'banana': 'banana',
        }
    }
})
dump(User())
dump(None)
# dd(range(0, 5))
