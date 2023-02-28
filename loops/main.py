NAMES = ["John", "Bob", "Mosh", "Sarah", "Mary"]
AGES = [20, 30, 40, 50, 60]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name}", f"{age}")