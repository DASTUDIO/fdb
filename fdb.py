class _fdbcls:

    data = {}

    def set(self, key, func, *args, **kwargs):
        self.data[key] = (func, args, kwargs)

    def get(self, key):
        func, args, kwargs = self.data[key]
        if len(args) == 0:
            if len(kwargs) == 0:
                return lambda: func()
            else:
                return lambda: func(**kwargs)
        else:
            if len(kwargs) == 0:
                return lambda: func(*args)
            else:
                return lambda: func(*args, **kwargs)

    def delete(self, key):
        del self.data[key]

_fdb = _fdbcls()

def set(key, func, *args, **kwargs):
    _fdb.data[key] = (func, args, kwargs)

def get(key):
    return _fdb.get(key)

def delete(key):
    _fdb.delete()