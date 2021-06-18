# Pylint

a = 1

def foo(hello):
    print(hello)

foo(a)

class A:
    pass

a = A()

def longfoo(a,
            c, name1=None):
    pass

d = {"key": 1,
     "ke1": 2, "value": {"key": True}
     }

for el in range(10):
    for el2 in range(11):
        for el3 in range(12):
            try:
                print(el + el2 + el3)
            except:
                pass