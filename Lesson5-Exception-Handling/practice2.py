# def safe_level_up(xp, hours_studied):
#     try:
#         new_level = xp // hours_studied
#         return new_level
#     except ZeroDivisionError:
#         print("No grind, no glory!")
#         return xp // 10

# print(safe_level_up(1000,5))
# print(safe_level_up(500,0))
# print(safe_level_up(750,3))

# def activiate_knowledge_crystal (code):
#     try:
#         value = int(code)
#         return value
#     except ValueError:
#         return 1
#     finally:
#         print("Crystal energy surge!")

# print(activiate_knowledge_crystal("42"))
# print(activiate_knowledge_crystal("magic"))
# print(activiate_knowledge_crystal("999"))

def join_study_squad(members):
    if members == "":
        print("Squad disbanded :(")
        return 0
    count = 1
    found_non_separator = False

    for char in members:
        if char == ",":
            count += 1
        else:
            found_non_separator = True
    
    if not found_non_separator: # if string only contains commas
        print("Squad disbanded :(")
        return 0
    
    return count

print(join_study_squad("Alice, Bob, Charlie"))
print(join_study_squad(",,,"))