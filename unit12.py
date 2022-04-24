#######################################################
# Name:       Michael Cunningham
# Class:      CIS-2531-VCM01
# Assignment: Homework 12
# Instructor: Mohammad Morovati
# Purpose:    recursion
######################################################

#setlimit
import sys
sys.setrecursionlimit(5000)
#defining function main
def recursum(n):
    if n <= 1:
        return n
    else:
        return n + recursum(n-1)
#take input
num = int(input("enter a number greater than zero less than 1,000: "))
#check that input greater than 0 or give the green light to exicute
if num < 0:
    print ("enter a positive integer of one or greater: ")
else:
    print("the sum is ", recursum(num))