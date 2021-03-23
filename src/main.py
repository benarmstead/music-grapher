import os
import sys
import csv
import time
import matplotlib.pyplot as plt

global your_path

def plotter(data, limit_to):
    label = []
    value = []

    length = len(data)
    #print(data)
    for i in range(length):
        label.append(data[i][0])
        value.append(data[i][1])

    if limit_to != -1:
        for i in range(length - limit_to):
            label.pop(0)
            value.pop(0)

    explode = []
    for i in range(len(label)):
        explode.append(0.1)

    plt.pie(value, labels = label, autopct='%1.0f%%', shadow = True, explode = explode)
    plt.show()

def wait():
    input("\nPress enter to continue: ")

def get_all_data():
    your_path = "/home/ben/Scripts/musicMonitor/music.csv"

    data = []

    with open(your_path, 'r') as file:
        for lines in csv.reader(file):
            data.append(lines)
    return data


def most_played(selection):
    data = get_all_data()
    selections = []
    for i in range(len(data)):
        selections.append(data[i][selection])
    selections.sort()

    selection_counted = []
    prev_selection = ""
    count = 1

    for i in range (len(selections)):
        current = selections[i]
        if current == prev_selection:
            count += 1

        else:
            selection_counted.append([prev_selection, count])
            count = 1
            prev_selection = current

    selection_counted.append([prev_selection, count])
    selection_counted.pop(0)


    def sorter(i):
        return i[1]

    return sorted(selection_counted, key = sorter)



def pretty_print(data):
    for i in range (len(data)):
        print(" | ".join(map(str, data[i])))

def get_total(selection):
    item = most_played(selection)

    total = 0
    item_count = 0

    for i in range(len(item)):
        total += item[i][1]
        item_count += 1

    return total, item_count

def menu():
    os.system("clear")

    print("""    1. Show whole table
    2. Most Played Songs
    3. Most Played Artists
    4. Average Songs Per Day
    5. Most Songs Played Per Day
    6. Total songs played & total unique songs played & avg plays p/song
    7. Exit"""
    )
#7. Clean CSV
#6. Most Songs Played of artist of choice
    try:
        choice = int(input(": "))
    except:
        print("Enter a number from 1-10")
        time.sleep(2)
        menu()

    os.system("clear")


    #selection = 0 #Songs
    #selection = 1 #Artists
    #selection = 2 #Albums
    #selection = 3 #Genre
    #selection = 4 #Avg Song length
    #selection = 5 #
    #selection = 6 #??
    #selection = 7 #Date???

    def execu(selection, limit_to):
        data = most_played(selection)
        pretty_print(data)
        plotter(data, limit_to)
        wait()

    if choice == 1:
        pretty_print(get_all_data())
        wait()

    elif choice == 2:
        execu(0, 25) # Set to -1 for all items to be on graph
    elif choice == 3:
        execu(1, 15) # Set to -1 for all items to be on graph
    elif choice == 4:
        total, dates_count = get_total(7)
        print("Avereage songs listened to per day: " + str(total/dates_count))
        wait()

    elif choice == 5:
        execu(7, 30)
    elif choice == 6:
        total, songs_count = get_total(0)
        print("Total number of songs listened to: " + str(total))
        print("Over " + str(songs_count) + " different songs")
        print("You play each song " + str(total/songs_count) + "x on average")
        wait()

    elif choice == 7:
        exit()


def init():
    if len(sys.argv) != 2:
        print("You must enter only 1 argument (the file path where your music.csv is)")
        exit()

    else:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("Help: python3 main.py ")
            exit()
        else:
            try:
                file = open(sys.argv[1])
            except FileNotFoundError:
                print(".csv containing music data not found!")
                exit()

        your_path = sys.argv[1]
        while 1:
            menu()

init()
