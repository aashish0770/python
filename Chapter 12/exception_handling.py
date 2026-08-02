# Exception handling
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(result)
# except ValueError:
#     print("Invalid input. Please enter a number.")
# # raise an exception
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# # try with else

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b

# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print(f"The result is: {result}")

# try with finally

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b

except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {result}")
# program execution will always reach this block, regardless of whether an exception occurred or not
finally:
    print("Program execution completed.")

# why use finally block in exception handling? 
# The finally block is used to ensure that certain code is executed regardless of whether an exception occurred or not. 
# It is typically used for cleanup actions, such as closing files, releasing resources, or performing any necessary finalization tasks. 
# This guarantees that important code runs even if an error occurs during the execution of the try block.
