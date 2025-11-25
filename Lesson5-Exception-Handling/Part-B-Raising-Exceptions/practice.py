def calculate_kd(kills, deaths):
    try:
        kd_ratio = kills / deaths
        return kd_ratio
    except ZeroDivisionError:
        print("Cannot calculate K/D")
        return 0

print(calculate_kd(20, 5))
print(calculate_kd(15, 0))

def process_donation(amount):
    if amount <= 0:
        raise ValueError ("Donation must be positive!")
    print(f"Thanks for ${amount}!")

try:
    process_donation(25)
    process_donation(-5)
    print("All donations processed!")
except ValueError as e:
    print(f"Error: {e}")

def create_gamertag(tag):
    if not tag:
        raise ValueError ("Empty tag")
    elif " " in tag:
        raise ValueError ("Contains space")
    elif len(tag) > 15:
        raise ValueError ("Tag is too long")
    return tag
  
try:
    print(create_gamertag("ShadowNinja"))
    print(create_gamertag("has spaces"))
    print(create_gamertag(""))
except ValueError as e:
    print(f"Error: {e}")

def split_bill(total_text, people):
    try:
        total = float(total_text)
        each = total / people
        return f"${each: .2f} per person"
    except ValueError:
        return "Enter a valid total!"
    except ZeroDivisionError:
        return "Need at least one person!"

print(split_bill("fifty", 4))
print(split_bill("20.00", 0))
print(split_bill("20.00", 4))