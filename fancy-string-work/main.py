greet = "Hello World"
extended_grt = "Hello World" + "this is a long string"

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formated = greet_format.format(name)

print(intrupution, formated)

print(formated.upper())
print(formated.lower())
print(formated.title())
print(formated.capitalize())
print(formated.replace("John", "Jane"))
