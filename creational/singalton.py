#######################################

            #Approch1

#######################################

from typing import Any


def singalton(cls):
    instance = {}
    def get_singalton(*args,**kwargs):
        if not instance.get(cls):
            instance[cls] = cls(*args,**kwargs)
            
        return instance[cls]
    return get_singalton 

@singalton
class A:
    a = 2 

a = A()
b = A()
print(a,b,a==b)
    

#########################################

           #Approch 2

########################################
class SingletonMeta(type):
    instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls.instance:
            cls.instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwds)
        return cls.instance[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        pass

print(Singleton() == Singleton())


#########################################

           #Approch 3

########################################


class Singalton:
    _instance = {}
    def __new__(cls,*args,**kwargs):
        if cls in cls._instance:
            return cls._instance[cls]
        cls._instance[cls]= super().__new__(cls,*args,**kwargs)
        return cls._instance[cls]

    def __init__(self):
        self.a = 1

a = Singalton()
b = Singalton()
print(a,b,a==b)