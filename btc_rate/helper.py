
class Singleton(type):
    instances = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.instances[cls]    