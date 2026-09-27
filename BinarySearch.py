marks = [22, 45, 67, 89, 98]

target = int(input("Enter element to search: "))

low = 0
high = len(marks) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if marks[mid] == target:
        print("Element found at position", mid + 1)
        found = True
        break

    elif marks[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element not found")