import keyboard
saly = []
try:
    test = int(input("Please enter how many saleries you would like: "))
except ValueError:
    print("Value must be an int!")


def addentry():
    count = 0
    c2 = 1
    while count < test:
        try:
            saly.append(int(input("Enter salary {}: ".format(c2))))
            count += 1
            c2 += 1
        except ValueError:
            print("Error: wrong value")
    saly.sort()


def listentry():
    c1 = 1
    for i in saly:
        print("Salary {}: {} SEK".format(c1, i))
        c1 += 1
