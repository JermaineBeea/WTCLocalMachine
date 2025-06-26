import math

def fibonacci(n:int) -> list:
    if n <= 0: return []
    a = 0; b = 1
    if n == 1: return [a]
    if n == 2: return[a, b]

    result = [a, b]
    for k in range(2, n):
        next = a + b
        a = b
        b = next
        result.append(b)
    
    return result

def factorial(n:int) -> int:
    if n < 0: return ""
    result = 1
    for k in range(n):
        result *= (k + 1)
    
    return result


def count_letters_and_punctuation(sentence: str) -> dict:
    sentence = ''.join(sentence.split())
    sentence = ''.join(filter(lambda n: not n.isdigit(), sentence.lower()))
    sentence = sorted(sentence)
    return {char: sentence.count(char) for char in sentence}



def is_square(number: int) -> bool:
    if number < 0: return False
    a = int(math.sqrt(number))
    return a*a == number

def count_perfect_squares_in_list(numbers: list) -> int:
    return sum([is_square(k) for k in numbers])



def is_prime(num):
    if num <= 0: return False
    if num == 1: return False
    if num == 2: return True

    for n in range(2, num):
        if num % n == 0: return False
    
    return True

def generate_primes(end: int) -> list:
    if end == 1: return [2]
    if end == 2: return [2, 3]
    odd = 3
    counter = 2
    primes = [2, odd]

    while counter < end:
        odd += 2
        if is_prime(odd):
            primes.append(odd)
            counter += 1
    
    return primes

def arithmetic_sum(number):
    return int(number * (number + 1) / 2)

def draw_triangle_prime(height: int) -> None:
    for n in range(height):
        start = arithmetic_sum(n)
        end = start + n
        print(*generate_primes(end + 1)[start:end + 1])



def is_palindrome_iterative(word: str) -> bool:
    word = list(filter(lambda n: n.isalnum(), word.lower()))
    word2 = word[::-1]
    for a,b in zip(word, word2):
        if a.lower() != b.lower():
            return False
    return True


def linear_sum(array1, array2):
    sum = 0
    for a,b in zip(array1, array2):
        sum += a*b
    return sum

def transpose(matrix):
    matrix3 = []
    for n in range(len(matrix[0])):
        innerArray = []
        for array in matrix:
            innerArray.append(array[n])
        matrix3.append(innerArray)
    return matrix3

def matrix_multiply(matrix1: list, matrix2: list) -> list:
    result = []
    for a in matrix1:
        inerResult = []
        for b in transpose(matrix2):
            inerResult.append(linear_sum(a, b))
        result.append(inerResult)
    return result
    



        

