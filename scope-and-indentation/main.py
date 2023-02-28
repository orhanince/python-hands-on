RUN_INTENDED = True

message = "running unintended"

if RUN_INTENDED:
    message = "running intended"

print(message)


def my_function():
    greet = "Hello"
    print(greet)


my_function()
print(my_function())