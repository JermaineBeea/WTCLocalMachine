
# TODO: return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape()-> str:
    
    valid_shapes = 'square', 'triangle', 'triangle_reversed', 'triangle_multiplication', 'pyramid', 'triangle_prime'
    while True:
        shape = input('Please enter shape to draw: ').lower().strip()
        if shape in valid_shapes:
            return shape
        else:
            print("Invalid shape. Please enter a valid shape.")


# TODO: return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height()->int:
    
    while True:

        try:
            height = input('Please enter height: ')
            height = int(height)
            if 1<= height <= 80:
                return height
            else:
                print('Please enter valid number')
        except ValueError:
            print('Please enter valid number')


# TODO: Complete the required shapes below
#       with reference to the unittests
def draw_square(height:int)->None:
    
    """
    Draws a square pattern of asterisks (*) with the given height and width.
    
    Parameters:
        height (int): The height and width of the square. Must be a positive integer.
        
    Returns:
        None: Prints the square pattern directly to console.
        
    """
    for _ in range(height):
        print('*' * height)


def draw_pyramid(height:int)->None:
    
    """
    Draws a centered pyramid pattern of asterisks (*) with the given height.
    
    Parameters:
        height (int): The height of the pyramid. Must be a positive integer.
        
    Returns:
        None: Prints the pyramid pattern directly to console.
        
    """
    
    for n in range(height):
        space = ' ' * (height - (n + 1))
        print(space + '*'*(2*n + 1))

def draw_triangle(height:int)->None:
    
    """
    Draws a number triangle where each row contains sequential numbers from 1 to the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the triangle pattern directly to console.
    
        
    """
    for n in range(height):
        print(*[k + 1 for k in range(n + 1)], '')
  


def draw_triangle_reversed(height:int)->None:
    
    """
    Draw an inverted number triangle where each row begins with its position number, 
    with the top row having the most repeated numbers and each row below having one fewer repetition.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the inverted triangle pattern directly to console.
        

    """
    
    for n in range(height):
        print(*[n + 1] * (height - n), '')



def draw_triangle_multiplication(height:int)->None:
    
    """
    Draws a multiplication triangle where each row shows products of the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the multiplication triangle pattern directly to console.
        
    """
    for n in range(height):
        print(*[(n + 1) * (k + 1) for k in range(n + 1)], '')
  

def draw_triangle_prime(height:int)->None:
    
    """
    Draws a triangle of prime numbers where each row contains the first n primes
    that fit the row width.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the prime number triangle pattern directly to console.
        
    """
    
    def isPrime(num: int) -> bool:
        if num < 0: return False
        if num == 1: return False
        if num == 2: return True

        for n in range(2, num):
            if num % n == 0: 
                return False
        
        return True
    
    def generatePrimes(end: int) -> list:
        if end == 0: return []
        if end == 1: return [2]
        odd = 3
        counter = 2
        primes = [2, odd]

        while counter < end:
            odd += 2
            if isPrime(odd):
                primes.append(odd)
                counter += 1

        return primes
    
    def arithmetic_sum(number: int) -> int:
        return int(number * (number + 1) / 2)
    
    for k in range(height):
        start = arithmetic_sum(k)
        end = start + k
        print(*generatePrimes(end + 1)[start : end + 1], '')

                
# TODO: add support for other shapes
def draw(shape:str, height:int)->None:
    
    """
    Main drawing function that calls the appropriate shape-specific drawing function
    based on the requested shape type.
    
    Parameters:
        shape (str): The type of shape to draw. Must be one of:
            - "square": A square of asterisks
            - "triangle_reversed": Inverted triangle of repeated row numbers
            - "triangle": Triangle of sequential numbers
            - "triangle_multiplication": Triangle of multiplication products
            - "pyramid": Centered pyramid of asterisks
            - "triangle_prime": Triangle of prime numbers
        height (int): The height of the shape. Must be a positive integer.
        
    Returns:
        None: Prints the requested shape pattern directly to console.
    """
    
    if shape == "pyramid":
        draw_pyramid(height)
    
    if shape == "square":
        draw_square(height)

    if shape == "pyramid":
        draw_pyramid(height)

    if shape == "triangle":
            draw_triangle(height)

    if shape == "triangle_reversed":
        draw_triangle_reversed(height)

    if shape == "triangle_multiplication":
            draw_triangle_multiplication(height)

    if shape == "triangle_prime":
        draw_triangle_prime(height)




# TODO: (standalone function) - Solve Pascal's Triangle
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """
    import math
    def combination(n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    
    return [combination(n, k) for k in range(n + 1)]


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)
    