from src.dd import dump, dd


class Permission:
    def __init__(self, name):
        self.name = name


class Role:
    def __init__(self, role):
        self.permission = Permission(role)


class User:
    classy = 1

    @property
    def dyno(self):
        return 1

    def __init__(self):
        self.stasis = 2
        self._password = 'password'
        self.__token = 'token'
        self.role = Role('admin')

    def fx(self):
        return 3


dd("Hello")
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

# dd(range(0, 5))
