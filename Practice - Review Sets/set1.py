# 1 - Code Tracing
"JORDAN JUST SCORED 45 POINTS!"
"THE CROWD GOES WILD!"

"LEILA JUST SCORED 28 POINTS!"
"THE CROWD GOES WILD!"

# 2 - Code Tracing
"1670"

# 3 - Code Writing
def generate_username(first, last):
    """Create username"""
    username = first[0].lower() + last.lower()
    if len(last) < 5:
        username += "1"
    return username

print(generate_username("Sydney, Montevirgen"))

# 4 - Code Tracing 
"Today: SUNNY, Tomorrow: COLD"

# 5 - Code Writing
def playlist_length(songs, average_duration):
    """Return total time in Xh Ym format"""
    total_min = len(songs) * average_duration
    hours = int(total_min // 60)
    minutes = int(total_min % 60)
    return f"{hours}hrs and {minutes}min"

print(playlist_length(["Bohemian Rhapsody"], 5.9))

# 6 - Code Tracing
"Total XP: 220"

# 7 - Code Writing
def battle_cry(hero, weapon, damage):
    """Generate battle message"""
    return f"{hero.upper()} swings {weapon.upper()} for {damage} damage"

print(battle_cry("Spiderman", "Web Slinger", 90))