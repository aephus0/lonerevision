from time import sleep, time
import keyboard
import statistics
import sys
from pynput.keyboard import Listener

saly = []


def addentry():
    test = 0
    try:
        test = int(input("Please enter how many saleries you would like: "))
        print("\n")
    except ValueError:
        print("Value must be an int!")
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
    n = 0
    while True:
        try:
            print("{} kr".format(saly[n]), end="\t")
            n += 1
            print("{} kr".format(saly[n]), end="\t")
            n += 1
            print("{} kr".format(saly[n]), end="\t")
            n += 1
            print("\n")
        except:
            break


def medel():
    x = int(round(sum(saly)/len(saly)))
    print("Medellön     :" + "{:>10}".format(x) + " SEK")


def median():
    print("Medianlön    :" +
          "{:>10}".format(int(statistics.median(saly))) + " SEK")


def spridning():
    z = max(saly) - min(saly)
    print("Lönespridning:" + "{:>10}".format(z) + " SEK")


def main():
    addentry()
    print("---------------------------------")
    medel()
    median()
    spridning()
    print("---------------------------------")
    listentry()
    while True:
        try:

            if keyboard.is_pressed('space'):
                print("\n")
                main()
                break
            elif keyboard.is_pressed('esc'):
                sys.exit()
        except ValueError:
            break


main()
