"""
Lesson 3: Return Values - Practice Exercises
"""

def greet(name):
    print(f"Hello {name}")
    return f"Hello {name}"

result = greet("Syd")
print(result)

# ** RETURN ENDS THE FUNCTION** 

def square(num):
    """Returns the square of a number."""
    return num ** 2
# Capture the returned value
result = square(5)
print(f"5 squared is {result}")
# Use it in a calculation
area = square(7) * 2
print(f"Area: {area}")

def get_letter_grade(percentage):
    """Returns letter grade based on percentage."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
result = get_letter_grade(80)
print(result)

# ============================================================================
# Practice 1: Rectangle Area
# ============================================================================
def rect_area(l, w):
    area = l * w
    return area

rect1 = rect_area(3,5)
print(f"Rectangle 1 Area: {rect1}")
rect2 = rect_area(8,9)
print(f"Rectange 2 Area: {rect2}")

# ============================================================================
# Practice 2: Temperature Converter
# ============================================================================
def celsius_to_fahrenheit(celsius):
    "convert Celsius to Farenheit"
    return (celsius*9/5) + 32

celsius1 = celsius_to_fahrenheit(38)
print(f"Faranheit Conversion: {celsius1}")



# ============================================================================
# Practice 3: Find Maximum
# ============================================================================

def find_max(num1, num2):
    """Return the larger of two numbers"""
    if num1 > num2:
        return num1
    return num2 # Alternative return max(num1, num2)

print(f"Max (3,5) = {find_max(3,5)}")

# ============================================================================
# Practice 4: Is Even?
# ============================================================================

def is_even(number):
    """Return True if number is even, False if odd."""
    # Method 1: Direct return (best!)
    return number % 2 == 0 

# ============================================================================
# Practice 5: Calculate Tip
# ============================================================================




# ============================================================================
# Challenge 1: Calculate Average
# ============================================================================





# ============================================================================
# Challenge 2: Letter Grade
# ============================================================================

