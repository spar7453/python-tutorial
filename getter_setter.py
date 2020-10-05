from dataclasses import dataclass

class Age:
    def __init__(self, age = 0):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age


age = Age(10)
print(f"age = {age.get_age()}")
age.set_age(20)
print(f"age = {age.get_age()}")

# This does not look good


class SimpleAge:
    def __init__(self, age = 0):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)

print("")
simple_age = SimpleAge(10)
print(f"age = {simple_age.age}")
simple_age.age = 20
print(f"age = {simple_age.age}")

class NewAge:
    def __init__(self, age = 0):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @age.deleter
    def age(self):
        del self._age


print("")
new_age = NewAge(10)
print(f"age = {new_age.age}")
new_age.age = 20
print(f"age = {new_age.age}")
