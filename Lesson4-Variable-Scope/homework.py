# 1 - Code Tracing
# print(update(val)) = 15
# print(val) = 10

# 2 - Code Tracing
# print(result) = 10

# 3 - Code Tracing
# print(outer_func(5)) = 10

# 4 - Code Tracing
# print(increment_counter()) = 4
# print(counter) = 4

# 5 - Code Tracing
# print (reset(score)) = 0 
# print(score) = 50

# 6 - Code Writing
def square_plus_one(n):
    value = n * n + 1
    return value
print (square_plus_one(5))

# 7 - Code Writing
def register_user(name, age):
    user = f"User {name}, {age} years old, registered"
    return user
print(register_user("Sydney", 16))

# 8 - Code Writing
my_list = ""
def update_global_list(item):
    global my_list
    my_list += item
    return my_list
print(update_global_list("Food"))

# 9 - Code Writing
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit
print(convert_to_fahrenheit(10))