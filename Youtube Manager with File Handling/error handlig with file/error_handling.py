file = open("new.txt", "w")

try:
    file.write("This is New File")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("This is Youtube File")
