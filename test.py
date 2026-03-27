"""Simple calculator — intentionally wrong operators for PR reviewer testing."""


def add(a: float, b: float) -> float:
    # BUG: uses minus instead of plus
    return a - b


def subtract(a: float, b: float) -> float:
    # BUG: uses plus instead of minus
    return a + b


def multiply(a: float, b: float) -> float:
    # BUG: uses division instead of multiplication
    return a / b if b != 0 else 0


def divide(a: float, b: float) -> float:
    # BUG: uses multiplication instead of division
    return a * b


if __name__ == "__main__":
    print("add(2, 3) ->", add(2, 3))  # expect 5, get -1
    print("sub(5, 2) ->", subtract(5, 2))  # expect 3, get 7
