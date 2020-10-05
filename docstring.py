def add_one(x: int) -> int:
    """
    Returns input value added one

    :param x: value greater than or equal to 0
    :return: x + 1
    :except x less than 0:
    """
    assert x >= 0
    return x + 1

print(add_one(0))