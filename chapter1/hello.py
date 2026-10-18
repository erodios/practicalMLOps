""" A basic python script to test Makefile. 
It has an add function that prints the results"""

def add(a, b):
    """Adds two numbers together"""
    return a + b


if __name__ == "__main__":
    result = add(2, 3)
    print(f"The result of adding 2 and 3 is: {result}")
