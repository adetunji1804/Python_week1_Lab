no_of_classes = int(input("How many Classes are you taking this semester: "))
class_name = []

for number in range(no_of_classes):
    input_list = input("Enter class name: ")
    class_name.append(input_list)
print("\n")
print("YOUR LIST OF CLASSES FOR THE SEMESTER\n--------------------------------------")
for list in class_name:
    print(list)
print("\n")