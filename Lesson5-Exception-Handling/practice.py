# 1 - Code Writing
def safe_multiply(x, y):
        if isinstance(x, (int,float)) and isinstance (y,(int, float)):
         return x * y
        return 0

print(safe_multiply(5,3))
print(safe_multiply(4, "a"))

# 2 - Code Tracing
# Zero Division Error: -1
# Print: -1

# 3 - Code Writing
def is_positive(value):
     try:
        return isinstance(value, (int,float)) and value > 0
     except:
         return False
          

print(is_positive(5))
print(is_positive(-3))
print(is_positive("hello"))

# 4 - Code Tracing
# Output: 0, TypeError
# Print: 0, Processing complete

# 5 - Code Writing
def format_message(code,text):
    try:
        return f"[{code}] {text}"
    except TypeError:
        return ("[ERROR] invalid")

print(format_message(404, "Not Found"))
print(format_message("none", "test"))

# 6 - Code Tracing
# Temp: 85 / 10 = 8.5 -> 8 (int) x 2 = 16
# Print: 16, Calculation done

# 7 - Code Writing
def safe_average (a, b):
    try:
        return (a + b) / 2
    except ZeroDivisionError:
        return 0

print (safe_average(10, 20))
print (safe_average (5, -5))

# 8 - Code Tracing
# Process Value: 60 - 55 = 5 * 10 = 50
# Print: 50, Process complete

# 9 - Code Tracing
# Value: TypeError, True x 100 = 0 
# Print: 10