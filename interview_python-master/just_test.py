
class MyClass(object):
    def __init__(self):
            self.__superprivate = "Hello"
            self._semiprivate = ", world!"
mc = MyClass()
print MyClass.__mro__
print MyClass.__class__
print type(MyClass)
# print mc._semiprivate
# print mc.__superprivate



# d = {key: value for (key, value) in iterable}
# d = {key: value for (key, value) in [[1,2],[3,4]]}



def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, curr + prev

# f = fib()
# print f
# print type(f)
# print f.next()
# print f.next()
# print f.next()


单例模式
class Sigleton(object):
    _state={}
    def __new__(cls, *args, **kwargs):
        ob = super(Sigleton,cls).__new__(cls,*args,**kwargs)
        ob.__dict__ = cls._state
        return ob

class Sigleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Sigleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance


map(lambda x:x*x,[1,2,3])


