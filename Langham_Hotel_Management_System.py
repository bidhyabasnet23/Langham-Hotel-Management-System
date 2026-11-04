#!/usr/bin/env python
# coding: utf-8

# In[1]:


# --------------------------------------------------
# LANGHAM HOTEL MANAGEMENT SYSTEM
# Student Name: Bidhya Basnet
# Student ID: 850008325
# Course: BBIM502 Introduction to Programming 
# Assessment: Assessment 2
# Date: 04 November 2026
# --------------------------------------------------

# Store room and allocation information

rooms = []
allocations = []

print("Welcome to Langham Hotel Management System")
print("Program started successfully.")


# In[2]:


# STEP 3: MAIN MENU

def show_menu():
    print("\n" + "*" * 65)
    print("              LANGHAM HOTEL MANAGEMENT SYSTEM")
    print("                         MAIN MENU")
    print("*" * 65)

    print("1. Add Rooms")
    print("2. Delete Rooms")
    print("3. Display Room Details")
    print("4. Allocate Rooms")
    print("5. Display Room Allocation Details")
    print("6. Billing and De-allocation")
    print("7. Save Room Allocation to a File")
    print("8. Display Room Allocation from a File")
    print("9. Backup and Clear Room Allocation File")
    print("0. Exit")

    print("*" * 65)


# Display the menu
show_menu()


# In[3]:


# STEP 4: ADD ROOMS

def add_rooms():
    print("\n--- ADD ROOMS ---")

    try:
        number = int(input("Enter room number: "))

        # Check if room already exists
        for room in rooms:
            if room["number"] == number:
                print("Room already exists!")
                return

        room_type = input("Enter room type (Standard/Deluxe/Suite): ")

        price = float(input("Enter price per night: "))

        if number <= 0 or price <= 0:
            print("Room number and price must be greater than zero.")
            return

        room = {
            "number": number,
            "type": room_type,
            "price": price,
            "allocated": False
        }

        rooms.append(room)

        print("Room added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")


# In[4]:


add_rooms()


# In[5]:


# STEP 5: DELETE ROOMS

def delete_rooms():
    print("\n--- DELETE ROOMS ---")

    try:
        number = int(input("Enter room number to delete: "))

        for room in rooms:
            if room["number"] == number:

                if room["allocated"] == True:
                    print("Room is allocated. Cannot delete!")
                    return

                rooms.remove(room)
                print("Room deleted successfully!")
                return

        print("Room not found!")

    except ValueError:
        print("Invalid input! Please enter a valid room number.")


# In[6]:


delete_rooms()


# In[7]:


# STEP 6: DISPLAY ROOM DETAILS

def display_rooms():
    print("\n--- ROOM DETAILS ---")

    if len(rooms) == 0:
        print("No rooms available.")
    else:
        print("Room Number\tRoom Type\tPrice\tStatus")
        print("-" * 60)

        for room in rooms:
            if room["allocated"] == True:
                status = "Allocated"
            else:
                status = "Available"

            print(room["number"], "\t\t",
                  room["type"], "\t\t",
                  "$", room["price"], "\t",
                  status)


# In[8]:


add_rooms()


# In[9]:


display_rooms()


# In[10]:


# STEP 7: ALLOCATE ROOMS

def allocate_rooms():
    print("\n--- ALLOCATE ROOMS ---")

    try:
        number = int(input("Enter room number: "))

        for room in rooms:
            if room["number"] == number:

                if room["allocated"] == True:
                    print("Room is already allocated!")
                    return

                customer_name = input("Enter customer name: ")
                nights = int(input("Enter number of nights: "))

                if customer_name.strip() == "" or nights <= 0:
                    print("Invalid customer name or number of nights!")
                    return

                allocation = {
                    "room_number": number,
                    "customer_name": customer_name,
                    "nights": nights,
                    "price": room["price"]
                }

                allocations.append(allocation)
                room["allocated"] = True

                print("Room allocated successfully!")
                return

        print("Room not found!")

    except ValueError:
        print("Invalid input! Please enter the correct details.")


# In[11]:


allocate_rooms()


# In[12]:


# STEP 8: DISPLAY ROOM ALLOCATION DETAILS

def display_allocations():
    print("\n--- ROOM ALLOCATION DETAILS ---")

    if len(allocations) == 0:
        print("No room allocations found.")

    else:
        print("Room Number\tCustomer Name\tNights\tPrice")
        print("-" * 60)

        for allocation in allocations:
            print(allocation["room_number"], "\t\t",
                  allocation["customer_name"], "\t\t",
                  allocation["nights"], "\t$",
                  allocation["price"])


# In[13]:


display_allocations()


# In[14]:


# STEP 9: BILLING AND DE-ALLOCATION

def billing():
    print("\n--- BILLING AND DE-ALLOCATION ---")

    try:
        number = int(input("Enter room number: "))

        for allocation in allocations:
            if allocation["room_number"] == number:

                total = allocation["price"] * allocation["nights"]

                print("\n--- CUSTOMER BILL ---")
                print("Customer Name:", allocation["customer_name"])
                print("Room Number:", number)
                print("Number of Nights:", allocation["nights"])
                print("Price Per Night: $", allocation["price"])
                print("Total Amount: $", total)

                allocations.remove(allocation)

                for room in rooms:
                    if room["number"] == number:
                        room["allocated"] = False

                print("Room de-allocated successfully!")
                return

        print("Room allocation not found!")

    except ValueError:
        print("Invalid input! Please enter a valid room number.")


# In[15]:


billing()


# In[16]:


# STEP 10: SAVE ROOM ALLOCATIONS TO FILE

def save_allocations():
    print("\n--- SAVE ROOM ALLOCATIONS ---")

    try:
        file = open("LHMS_850008325.txt", "a")

        for allocation in allocations:
            file.write("Room Number: " + str(allocation["room_number"]) + "\n")
            file.write("Customer Name: " + allocation["customer_name"] + "\n")
            file.write("Number of Nights: " + str(allocation["nights"]) + "\n")
            file.write("Price Per Night: $" + str(allocation["price"]) + "\n")
            file.write("-" * 40 + "\n")

        file.close()

        print("Room allocations saved successfully!")

    except IOError:
        print("Error saving allocation file!")


# In[17]:


allocate_rooms()


# In[18]:


save_allocations()


# In[19]:


# STEP 11: DISPLAY ALLOCATIONS FROM FILE

def display_file():
    print("\n--- ROOM ALLOCATIONS FROM FILE ---")

    try:
        file = open("LHMS_850008325.txt", "r")

        details = file.read()

        if details == "":
            print("File is empty.")
        else:
            print(details)

        file.close()

    except FileNotFoundError:
        print("Allocation file not found!")

    except IOError:
        print("Error reading allocation file!")


# In[20]:


display_file()


# In[21]:


# STEP 12: BACKUP AND CLEAR ALLOCATION FILE

from datetime import datetime

def backup_file():
    print("\n--- BACKUP AND CLEAR FILE ---")

    try:
        file = open("LHMS_850008325.txt", "r")
        details = file.read()
        file.close()

        if details == "":
            print("No data available to backup.")
            return

        date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_name = "LHMS_850008325_Backup_" + date_time + ".txt"

        backup = open(backup_name, "w")
        backup.write(details)
        backup.close()

        file = open("LHMS_850008325.txt", "w")
        file.close()

        print("Backup created successfully!")
        print("Backup file name:", backup_name)
        print("Original allocation file cleared successfully!")

    except FileNotFoundError:
        print("Allocation file not found!")

    except IOError:
        print("Error creating backup file!")


# In[22]:


backup_file()


# In[23]:


# STEP 13: EXCEPTION HANDLING

def test_errors():
    print("\n--- ERROR HANDLING TEST ---")

    try:
        number = int(input("Enter a room number: "))
        print("Room number:", number)

    except ValueError:
        print("ValueError: Please enter numbers only.")

    try:
        name = input("Enter customer name: ")

        if name == "":
            raise ValueError("Customer name cannot be empty.")

        print("Customer name:", name)

    except ValueError as error:
        print("Error:", error)


test_errors()


# In[24]:


# STEP 14: TEST DIFFERENT EXCEPTIONS

import math

print("\n--- EXCEPTION HANDLING TEST ---")

# 1. SyntaxError
try:
    compile("if True print('Hello')", "<string>", "exec")
except SyntaxError:
    print("SyntaxError handled successfully.")

# 2. ValueError
try:
    int("hello")
except ValueError:
    print("ValueError handled successfully.")

# 3. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError handled successfully.")

# 4. IndexError
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("IndexError handled successfully.")

# 5. NameError
try:
    print(student_name)
except NameError:
    print("NameError handled successfully.")

# 6. TypeError
try:
    result = "Hello" + 10
except TypeError:
    print("TypeError handled successfully.")

# 7. OverflowError
try:
    math.exp(10000)
except OverflowError:
    print("OverflowError handled successfully.")

# 8. IOError
try:
    file = open("invalid_folder/test.txt", "w")
except IOError:
    print("IOError handled successfully.")

# 9. ImportError
try:
    from unknown_module import unknown_function
except ImportError:
    print("ImportError handled successfully.")

# 10. EOFError
try:
    raise EOFError
except EOFError:
    print("EOFError handled successfully.")

# 11. FileNotFoundError
try:
    file = open("missing_file.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError handled successfully.")

print("All exception tests completed.")


# In[25]:


# STEP 15: MAIN PROGRAM

while True:

    show_menu()

    try:
        choice = int(input("Enter your choice (0-9): "))

        if choice == 1:
            add_rooms()

        elif choice == 2:
            delete_rooms()

        elif choice == 3:
            display_rooms()

        elif choice == 4:
            allocate_rooms()

        elif choice == 5:
            display_allocations()

        elif choice == 6:
            billing()

        elif choice == 7:
            save_allocations()

        elif choice == 8:
            display_file()

        elif choice == 9:
            backup_file()

        elif choice == 0:
            print("Thank you for using Langham Hotel Management System.")
            break

        else:
            print("Invalid choice! Please select between 0 and 9.")

    except ValueError:
        print("Invalid input! Please enter a number.")


# In[ ]:




