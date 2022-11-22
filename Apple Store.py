iphone_list = ["iPhone 14 ", "iPhone 14 Plus", "iPhone 14 Pro ","iPhone 14 Pro Max"]
ipad_list = ["iPad 10th","iPad Air 5th","iPad Pro 11-inch","iPad Pro 12.9-inch"]
macbook_list = ["Macbook Air M1-chip", "Macbook Air M2-chip", "Macbook Pro 13-inch","Macbook Pro 14-inch "]
watch_list = ["Apple Watch 8th", "Apple Watch SE", "Apple Watch Ultra"]

iphone_prices = [799,899,999,1099]
ipad_prices = [449,599,799,1099]
macbook_prices = [999,1199,1299,1999]
watch_prices = [349,249,799]

your_cost = []
your_selections = []
count = 0
total_cost = 0
making_selection = True

def thumbnail():
    print(" ")
    print("***Welcome to Apple Store***")
    print(" ")
    print(" ⭐====|🍎|====⭐")
    print("| 1. iPhone    |")
    print("| 2. iPad      | ")
    print("| 3. Macbook   | ")
    print("| 4. Watch     |")
    print("| 5. Exit      |")
    print("~~⭐~~~⭐~~~⭐~~ ")

def iphone():
        print(" ")
        print("       ⭐========|📱|========⭐")
        print("| 1. iPhone 14          $799     |")
        print("| 2. iPhone 14 Plus     $899     | ")
        print("| 3. iPhone 14 Pro      $999     | ")
        print("| 4. iPhone 14 Pro Max  $1099    |")
        print("| 5.           Exit              |")
        print("    ~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~ ")



def ipad():
    print(" ")
    print("     ⭐==========|🖥|==========⭐")
    print("| 1. iPad 10th           $449     |")
    print("| 2. iPad Air 5th        $599     | ")
    print("| 3. iPad Pro 11-inch    $799     | ")
    print("| 4. iPad Pro 12.9-inch  $1099    |")
    print("| 5.           Exit               |")
    print("    ~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~ ")



def macbook():
    print("      ⭐=========|💻|=========⭐")
    print("| 1. Macbook Air M1-chip    $999     |")
    print("| 2. Macbook Air M2-chip    $1199    |")
    print("| 3. Macbook Pro 13-inch    $1299     |")
    print("| 4. Macbook Pro 14-inch    $1999    |")
    print("| 5.             Exit                |")
    print("    ~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~ ")



def watch():
    print(" ")
    print("    ⭐==========|⌚|==========⭐")
    print("| 1. Apple Watch 8th    $349     |")
    print("| 2. Apple Watch SE     $249     | ")
    print("| 3. Apple Watch Ultra  $799     | ")
    print("| 4.            Exit             |")
    print("   ~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~ ")




while(making_selection == True):
    thumbnail()
    option = input("Please select your option: ")
    if option == "1":
        iphone()
        iphone = input("Please make a select: ")
        if iphone == "1":
            your_selections.append(iphone_list[0])
            your_cost.append(iphone_prices[0])
            count += 1
            total_cost = total_cost + iphone_prices[0]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            print("~~⭐~~~⭐~~~⭐~~~⭐~~~⭐~~")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif iphone == "2":
            your_selections.append(iphone_list[1])
            your_cost.append(iphone_prices[1])
            count += 1
            total_cost = total_cost + iphone_prices[1]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif iphone == "3":
            your_selections.append(iphone_list[2])
            your_cost.append(iphone_prices[2])
            count += 1
            total_cost = total_cost + iphone_prices[2]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif iphone == "4":
            your_selections.append(iphone_list[3])
            your_cost.append(iphone_prices[3])
            count += 1
            total_cost = total_cost + iphone_prices[3]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        else:
            making_selection = True
    elif option == "2":
        ipad()
        ipad = input("Please make a select: ")
        if ipad == "1":
            your_selections.append(ipad_list[0])
            your_cost.append(ipad_prices[0])
            count += 1
            total_cost = total_cost + ipad_prices[0]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif ipad == "2":
            your_selections.append(ipad_list[1])
            your_cost.append(ipad_prices[1])
            count += 1
            total_cost = total_cost + ipad_prices[1]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif ipad == "3":
            your_selections.append(ipad_list[2])
            your_cost.append(ipad_prices[2])
            count += 1
            total_cost = total_cost + ipad_prices[2]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif ipad == "4":
            your_selections.append(ipad_list[3])
            your_cost.append(ipad_prices[3])
            count += 1
            total_cost = total_cost + ipad_prices[3]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        else:
            making_selection = True
    elif option == "3":
        macbook()
        macbook = input("Please make a select: ")
        if macbook == "1":
            your_selections.append(macbook_list[0])
            your_cost.append(macbook_prices[0])
            count += 1
            total_cost = total_cost + macbook_prices[0]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif macbook == "2":
            your_selections.append(macbook_list[1])
            your_cost.append(macbook_prices[1])
            count += 1
            total_cost = total_cost + macbook_prices[1]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif macbook == "3":
            your_selections.append(macbook_list[2])
            your_cost.append(macbook_prices[2])
            count += 1
            total_cost = total_cost + macbook_prices[2]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif macbook == "4":
            your_selections.append(macbook_list[3])
            your_cost.append(macbook_prices[3])
            count += 1
            total_cost = total_cost + macbook_prices[3]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        else:
            making_selection = True
    elif option == "4":
        watch()
        watch = input("Please make a select: ")
        if watch == "1":
            your_selections.append(watch_list[0])
            your_cost.append(watch_prices[0])
            count += 1
            total_cost = total_cost + watch_prices[0]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif watch == "2":
            your_selections.append(watch_list[1])
            your_cost.append(watch_prices[1])
            count += 1
            total_cost = total_cost + watch_prices[1]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        elif watch == "3":
            your_selections.append(watch_list[2])
            your_cost.append(watch_prices[2])
            count += 1
            total_cost = total_cost + watch_prices[2]
            print(" ")
            print(" ⭐=======|?|=======⭐")
            print("| 1.    Continue     |")
            print("| 2.      Exit       |")
            ask = input("Do you want to continue: ")
            if ask == "2":
                print(" ")
                print("⭐======|?|======⭐")
                print("| 1.    yes     |")
                print("| 2.    no      |")
                print("~~⭐~~~⭐~~~⭐~~~⭐~~")
                answer = input("Do you want to checkout : ")
                if answer == "1":
                    making_selection = False
                else:
                    making_selection = True
        else:
            making_selection = True
    else:
        if count >= 1:
          print(" ")
          print("⭐======|?|======⭐")
          print("| 1.    yes     |")
          print("| 2.    no      |")
          print("~~⭐~~~⭐~~~⭐~~~⭐~~")
          answer = input("Do you want to checkout : ")
          if answer == "1":
            making_selection = False
          else:
            making_selection = True
        else:
            break

def checkout(receipt):
    print("-----------")
    n = 0
    while (n<count):
        if receipt == your_selections:
            print("Item: " + str(receipt[n]))
            n = n+1
        else:
            print("Cost: " + str(receipt[n]) + "$")
            n = n + 1

print(" ")
print("Here is your receipt")
checkout(your_selections)
checkout(your_cost)

print("-----------")
print("The final cost is " + str(total_cost) + "$")