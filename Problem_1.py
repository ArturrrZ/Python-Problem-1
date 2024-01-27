"""
Given an array of N integers, your task is to transform this array into a permutation of the first N positive integers.
A permutation of size N is an arrangement of numbers such that each number from 1 to N appears exactly once.
In one operation, you can increase or decrease any element of the array by 1.
The challenge is to figure ot the smallest number of such operations require to convert the given array into a permutation.
Examples:
    1. Input: N=[3,2,1,4]
    Output: 0
    Explanation: No, operation needed, already a permutation.
    2. Input N=[4,1,4,2]
    Output: 1
    Explanation: Decrease one '4' to '3' to form the permutation: [4,1,3,2]
    Constraints: The integers in the array N will be equal or bigger than 1.
    The size of the array N can range from 1 to 10^5.
"""
def min_steps_to_solve(array):
    """
    write your answer
    """
    return #smth
#checking
if __name__=="__main__""":
    inp=input("Type array. Example: 1234\n")
    array_to_check=[]
    for i in inp.strip():
        i=int(i)
        array_to_check.append(i)
    min_steps_to_solve(array_to_check)
