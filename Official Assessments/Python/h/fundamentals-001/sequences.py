import math
"""
### Sequences

`sequences.py`

Create this file with the following functionality:

- A function that generates factorials: `generate_factorial_series(n: int) -> list`
    - `generate_factorial_series(4) -> [1, 2, 6, 24]`

- A function that generates the first `n` multiples of a multiplier: `generate_multiples(n: int, multiplier: int) -> list`

    - Example: `generate_multiples(5, 3) -> [3, 6, 9, 12, 15]`

---"""

def factorial(num):
    return math.factorial(num)



def generate_factorial_series(n: int) -> list:
  return [factorial(num + 1) for num in range(n)]


def generate_multiples(n: int, multiplier: int) -> list:
    return [multiplier * (k + 1) for k in range(n)]




