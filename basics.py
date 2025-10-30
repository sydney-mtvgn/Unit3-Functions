# Defining a function
def function_name():
  pass
# Calling a function
function_name()

def print_header():
  print("="*20)
  print("Student Report")
  print("="*20)

print_header()

# Empty Line
print("\n")

def draw_square():
# Draws a 5x5 square using asterisks
# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")

  for i in range(5):
   print("*****")

def morning_routine():
  print("Brush teeth and change")
  print("Pack bag and make bed")
  print("Drive to school")
pass

def school_schedule():
  print("History, English, Business")
  print("Compsci, Lunch, Bio")
  print("Gym, Stats")
pass

def after_school():
  print("Volleyball")
  print("Homework")
  print("Shower and eat")
pass

def daily_routine():
  morning_routine()
  print()
  school_schedule()
  print()
  after_school()

daily_routine()

