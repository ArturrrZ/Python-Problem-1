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
    original_array=array
    print(original_array)
    single_digits=[]
    repeated_digits=[]
    amount_of_operations=0
    for index,i in enumerate(array):
        if i in single_digits:
            repeated_digits.append({"digit":i,
                                    "index":index})
        else:
            single_digits.append(i)

    if len(repeated_digits)==0:
        print("No operations needed. Already a permutation.")
        return 0
    for bad_num_dict in repeated_digits:
        num_to_incr=bad_num_dict["digit"]
        index=bad_num_dict["index"]
        num_to_decr=num_to_incr

        operations_to_incr=0
        operations_to_decr=0
        is_not_able_to_deacrese=False
        # array[index]=num
        while num_to_incr in single_digits:
            num_to_incr+=1
            operations_to_incr+=1
        while num_to_decr in single_digits:
            num_to_decr-=1
            operations_to_decr+=1
            if num_to_decr==0:
                is_not_able_to_deacrese=True

        if is_not_able_to_deacrese or operations_to_decr > operations_to_incr:
            #replace
            array[index] = num_to_incr
            single_digits.append(num_to_incr)
            amount_of_operations += operations_to_incr
        else:
            array[index] = num_to_decr
            single_digits.append(num_to_decr)
            amount_of_operations += operations_to_decr

    print("Single Digits:", single_digits)
    print("Repeated Digits:", repeated_digits)
    print("Transformed Array:", array)
    print(f"Smallest amount of operations: {amount_of_operations}")
    return amount_of_operations

#checking
if __name__=="__main__":
    inp=input("Type array. Example: 1234\n")
    array_to_check=[]
    inp=inp.strip()
    for i in inp:
        i=int(i)
        array_to_check.append(i)
    min_steps_to_solve(array_to_check)