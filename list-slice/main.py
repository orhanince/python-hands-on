NAMES = ["John", "Bob", "Mosh", "Sarah", "Mary"]
AGES = [20, 30, 40, 50, 60]

JOHN = NAMES[0]
BOB = NAMES[1]

JOHN_BOB = NAMES[:2]
SARAH_MARY = NAMES[3:]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]
print(JOHN)
print(BOB)
print(JOHN_BOB)
print(SARAH_MARY)
print(REVERSE)
print(EVERY_OTHER)
print(sum(AGES))
print(max(AGES))
print(min(AGES))
