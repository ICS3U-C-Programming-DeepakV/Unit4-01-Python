#!/usr/bin/envpython3
# Created By:Deepak
# Date: 11/02/2026
# This program writes loops

import constants


def main():

    total_num = 0
    counter_loop = 0
    # asking the user to input the number of loops they want.
    user_loop_str = input("Enter the number of loops you want: ")
    # trying to convert the user's input into a string
    try:
        user_loop = int(user_loop_str)
        # if the user's input is converted to a string, this code will check if it's below 0
        if user_loop < 0:
            print("Integer can not be a negative number.")
        # else it will just start a loop and track the loop the amount of times the user's number
        else:
            while counter_loop < user_loop:
                counter_loop += 1
                total_num = total_num + counter_loop
                print(f"Tracking {counter_loop} times through a loop")
            print(f"The sum of the numbers from 0-{user_loop} is {total_num}.")
    # If none work, it will declare the user's input has not a valid integer
    except:
        print(f"{user_loop} is not a valid integer")


if __name__ == "__main__":
    main()
