first = input("enter first name: ")
last = input("enter last name: ")
mini = min(first, last)
print(mini)
for i in range(0, len(mini)):
    firstname = ""
    lastname = ""
    new = "#"
    for j in range(0, i+1):
        firstname = firstname + first[j]
        lastname = lastname + last[j]
    new = new+firstname+lastname
    print(new)