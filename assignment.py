def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"
    
#print (format_string("Bijay Rai", 26))

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return ("Greater")
    
    elif number < 10:
       return ("Lesser")

    else:
        return ("Equal")

#conditional_check(23) 

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0                     #Initializing the number

    for i in range (1, n+1):    #loopc starts from 1 and end to n+1
        sum += i                #Adding i to sum
    
    return sum                  #returning the total

#loop_sum(6)

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total = sum(numbers)
    large = max(numbers)
    small = min(numbers)

    return (total, large, small)

#print(list_operations([1, 2, 3, 4, 5]))


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    result = []

    for i in students_dict:
        if students_dict[i] > 80:
            result.append(i)
    
    return result

# students = {
#         "John": 85,
#         "Alice": 90,
#         "Bob": 75,
#         "Eve": 95
# }

# print (dict_operations(students))

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return set(list1) & set(list2)

#print(set_operations([1, 2, 3], [2, 3, 4]))

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {"sum": a + b,
            "difference": a - b,
            "product": a * b,
            "quotient": a / b}
#print(arithmetic_ops(10, 5))

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return{"and": x and y,
           "or": x  or y,
           "not_x": not x}

#print(logical_ops(True, False))

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {"and": a & b,
            "or": a | b,
            "xor": a ^ b
            }
#print(bitwise_ops(12, 10))