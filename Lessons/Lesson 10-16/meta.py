sc = type('SimpleClass', (), {"attr": 10})
x = sc()
print(x.attr)

"""
class SimpleClass:
    attr = 10 
"""

new_class = type('NewClass', (sc,), {})
x = new_class()
print(x.attr)

"""
class NewClass(SimpleClass): pass
"""

def func(obj):
    print(obj.attr)

cc = type('ComplexClass', (sc,), {"print_attr": func})
x = cc()
x.print_attr()

"""
class ComplexClass(SimpleClass):
    def print_attr(self):
        print(self.attr)
"""

class Meta(type):
    def __new__(self, name, base, dict):
        x = super().__new__(self, name, base, dict)
        x.attr = 100
        return x

class MyClass(metaclass=Meta): pass
x = MyClass()
print(x.attr)
