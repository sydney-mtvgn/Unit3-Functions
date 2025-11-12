# 1 - Code Tracing
"FINAL SCORE: 1500"

# 2 - Code Tracing
"FIRE"
"WARM"
"HOT"

# 3 - Code Writing
def generate_hashtag(phrase):
    title = phrase.title()
    no_space = title.replace(" ", " ")
    hashtag = "#" + no_space

    if len(hashtag) > 20:
        return "TOO LONG"
    return hashtag

print(generate_hashtag("this is way too long for a hashtag"))

# 4 - Code Tracing
"GOAL SMASHED"

# 5 - Code Writing
def battle_cry(hero, weapon, damage):
    message = f"{hero.upper()} swings {weapon.upper()} for {damage} damage"
    if damage > 80:
        message += "CRITICAL HIT!"
    return message

print(battle_cry("Draco", "Fire Sword", 95))

# 6 - Code Tracing
"AI feels excited"
"I'm so HAPPY today!"

# 7 - Code Writing
def weather_alert(temp, wind):
    alert = ""
    if temp > 30:
        alert += "STAY HYDRATED"
    if temp < 5:
        if alert:
            alert += " + "
        alert += "BUNDLE UP"
    if wind > 40:
        if alert:
            alert += " + "
        alert += "HOLD ON TO YOUR HAT"

    if not alert:
        return "ENJOY THE WEATHER"
    return alert