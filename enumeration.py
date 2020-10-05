from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)  # Color.RED
print(Color.GREEN)  # Color.GREEN
print(Color.BLUE)  # Color.BLUE

print("")

print(Color.RED.value)  # 1
print(Color.GREEN.value)  # 2
print(Color.BLUE.value)  # 3

print("")

print(Color(1))  # Color.RED
print(Color(2))  # Color.GREEN
print(Color(3))  # Color.BLUE

