def nth_root(x, n):
    """
    Calculates the nth root of a number x.
    
    Parameters:
    - x: the number whose root is to be calculated
    - n: the degree of the root (e.g., 2 for square root, 3 for cube root)

    Returns:
    - The nth root of x
    """
    # The nth root of a number x is mathematically represented as x^(1/n)
    # Python allows exponentiation using the ** operator
    return x ** (1/n)







import math  # Importing math module to use the square root function

def euclidean_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points.
    
    Parameters:
    - point1: tuple or list of coordinates (e.g., [x1, y1])
    - point2: tuple or list of coordinates (e.g., [x2, y2])
    
    Returns:
    - Euclidean distance between the points
    """
    
    # Ensure both points are in the same dimension (e.g., 2D, 3D, etc.)
    if len(point1) != len(point2):
        raise ValueError("Points must be of the same dimension")
    
    # Calculate the sum of the squared differences between corresponding coordinates
    # For example, (x2 - x1)^2 + (y2 - y1)^2 + ...
    squared_diff_sum = sum((a - b) ** 2 for a, b in zip(point1, point2))
    
    # Return the square root of the sum to get the Euclidean distance
    return math.sqrt(squared_diff_sum)
