from dataclasses import dataclass

@dataclass # code does not run without this annotation
class Test:
    a: int
    b: int


t = Test(1, "b")

print(t.a) # 1
print(t.b) # b // note that python does not consider types
print(t) # Test(a=1, b='b')

print("")

# Above class is equivalent to
class Test2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.__class__.__name__}' f'(a={self.a!r}, b={self.b!r})'

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.a, self.b) == (other.a, other.b)


t2 = Test2(1, 'b')

print(t2.a)  # 1
print(t2.b)  # b
print(t2)  # Test(a=1, b='b')
t2.a = 2
print(t2)  # Test(a=2, b='b')


