marks = [22, 45, 67, 89, 98]

target = int(input("Enter element to search: "))

found = False

for i in range(len(marks)):
    if marks[i] == target:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")