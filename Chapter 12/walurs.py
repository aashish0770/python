# using walrus operator
# its a convenient way to assign values to variables as part of a larger expression
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Length is {n}, which is greater than 3.")
    # Length is 5, which is greater than 3.

# Type defination
n: int = 5
name: str = "hello"


# defining the variables types and return type in the function head
def sum(a: int, b: int) -> int:
    return a + b


print(sum(1, 2))  # 3

# adv type hinting
from typing import List, Dict, Tuple, Union, Optional

# list of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# dictionary with string keys and integer values
data: Dict[str, int] = {"a": 1, "b": 2, "c": 3}

# tuple of integers
coordinates: Tuple[int, int] = (1, 2)

# union type hinting
value: Union[int, str] = "ID23S"
value = 42  # can also be an integer

# optional type hinting
name: Optional[str] = None


# Match Cases
name = "Alice"
match name:
    case "Alice":
        print("Hello, Alice!")
    case "Bob":
        print("Hello, Bob!")
    case _:
        print(f"Hello, anonymous user! {name}")


# for satus code
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


print(http_status(9900))

# Dictionary merge using walrus operator
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = d1 | d2
print(d3)

# Exception handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid input. Please enter a number.")
# raise an exception
except ZeroDivisionError:
    print("Cannot divide by zero.")
