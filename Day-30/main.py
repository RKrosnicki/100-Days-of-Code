# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

height = float(input("Height in meters: "))
weight = float(input("Weight in kilograms: "))

if height > 2.5:
    raise ValueError("Human Height should not be over 2.5m")

bmi = weight / height ** 2

print(bmi)
