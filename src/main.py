import os
import sys
import csv
import time
import datetime
import matplotlib.pyplot as plt

# Plots the data to a chart aswell as limiting it to e.g. top 10 songs if neccecary
def plotter(data, limit_to):
    label = []
    value = []
    
    length = len(data)
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

    plt.bar(height = value, x = label)
    plt.xticks(rotation = 45)
    plt.show()

# Waits for user input
def wait():
    input("\nPress enter to continue: ")

# Returns the whole CSV as a list

def get_all_data():
    data = []
    with open(sys.argv[1], 'r') as file:
        for lines in csv.reader(file):
            data.append(lines)
    return data
# Iterates through the data, and groups togethor values and counts them 
def most_played(selection, data):
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


# Prints data nicely
def pretty_print(data):
    for i in range (len(data)):
        print(" | ".join(map(str, data[i])))

# Gets the total of an selection and returns it, aswell as the amount of items.
def get_total(selection):
    item = most_played(selection, get_all_data())

    total = 0
    item_count = 0

    for i in range(len(item)):
        total += item[i][1]
        item_count += 1
    
    return total, item_count

def pltr():
    plt.title('Day vs Songs Played of Band')
    plt.xlabel('Day')
    plt.ylabel('Songs Played')
    plt.xticks(rotation = 45)
    plt.legend()
    plt.show()


def execu(selection, limit_to, data):
    data = most_played(selection, data)
    pretty_print(data)
    plotter(data, limit_to)
    wait()


def pie_animation(selection, limit_to):
    
    limiter = 10
    for i in range(int(round(len(open(sys.argv[1]).readlines(  )) / 10))):
        count = 0
        data = []
        with open(sys.argv[1], 'r') as file:
            for lines in csv.reader(file):
                data.append(lines)
                count += 1
                if count > limiter:
                    break

        plotter_multi(most_played(selection, data), limit_to, i)
        limiter += 10
        

def plotter_multi(data, limit_to, filename):
    label = []
    value = []
    
    length = len(data)
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
    plt.savefig("images/" + str(filename) + ".png", dpi=320)
    plt.clf()


def menu():
    os.system("clear")
    
    # Prints the menu
    print("""    1. Show whole table
    2. Most Played Songs
    3. Most Played Artists
    4. Average Songs Per Day
    5. Most Songs Played Per Day
    6. Total songs played & total unique songs played & avg plays p/song
    7. Line graph of listening over time (Coming soon)
    8. Create a video animation of your listening habbits
    9. Exit"""
    )
    
    # Future additions
    #7. Clean CSV
    #6. Most Songs Played of artist of choice
    
    # Ensures input is int
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
    

    # Carrys out the functions needed to print all the data for an item.

    # Prints the whole table
    if choice == 1:
        pretty_print(get_all_data())
        wait()
    
    # Prints the most played songs and draws graph on them
    elif choice == 2:
        execu(0, 25, get_all_data()) # Set to -1 for all items to be on graph

    # Prints the most played artists and draws graph on them
    elif choice == 3:
        execu(1, 14, get_all_data()) # Set to -1 for all items to be on graph
    
    # Prints the average songs played per day
    elif choice == 4:
        total, dates_count = get_total(7)
        print("Avereage songs listened to per day: " + str(total/dates_count))
        wait()

    # Prints the most played songs per day and draws graph on them
    elif choice == 5:
        execu(7, 30, get_all_data())

    # Prints the Total songs played & total unique songs played & avg plays p/song
    elif choice == 6:
        total, songs_count = get_total(0)
        print("Total number of songs listened to: " + str(total))
        print("Over " + str(songs_count) + " different songs")
        print("You play each song " + str(total/songs_count) + "x on average")
        wait()

    elif choice == 7:
        print("Coming soon")
        #create_lines()

    # Exits
    elif choice == 8:
        if not os.path.exists("images"):
            os.makedirs("images")
        def starter(selection, limit_to):
            print("Processing...")
            pie_animation(selection, limit_to)
            print("Creating video...")
            os.system("ffmpeg -f image2 -i images/%d.png video" + str(selection) + ".mp4")
            os.system("xdg-open video" + str(selection) + ".mp4")

        starter(1, 14)
        starter(0, 25)

    elif choice == 9:
        exit()


# Ensures theat the program gets the correct .csv path input, then starts the program
def init():
    # Ensures the correct amount of arguments are passed
    if len(sys.argv) != 2:
        print("You must enter only 1 argument (the file path where your music.csv is)")
        exit()
    
    else:
        # If help needed, prints help
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("Help: python3 main.py <file path to .csv containing music  data>")
            exit()

        else:
            # Tests if the file passed exists, if not, alerts the user
            try:
                file = open(sys.argv[1])
            except FileNotFoundError:
                print(".csv containing music data not found!")
                exit()
    
        # If here is reached then the argument passed must be good, so starts the main program
        while 1:
            menu()

init()
