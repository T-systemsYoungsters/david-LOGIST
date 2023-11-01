# David Vilhena Klein
# 18.10.2023
# Lab 9 on http://programarcadegames.com

import random

#auxilary funtion that returns the smallest out of 3 parameters
def min3(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3

#auxilary funtion that prints a box with given height
def box(height,width):
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print()

#take list of numbers and return position of key
def find(list, key):
    for i in range(len(list)):
        if list[i] == key:
            print("Found", list[i], "at position", i+1)

#create a list of a given size with random integers from 1-5
def create_list(size):
    new_list=[]
    for i in range(size):
        new_list.append(random.randint(1,6))
    return new_list

#do the count() function as another function
def count_list(list, number):
    return list.count(number)

def average_list(list):
    return sum(list)/len(list)

def main():
    list = create_list(10000)
    for i in range(1,7):
        print(count_list(list,i))
    print("The average of all 10.000 numbers is", average_list(list))

if __name__=="__main__":
    main()