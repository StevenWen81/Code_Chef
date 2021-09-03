'''
Question:
Implement the function unique_in_order which takes as 
argument a sequence and returns a list of items without 
any elements with the same value next to each other and p
reserving the original order of elements.

Sample Test Case:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''

def unique_in_order(iterable):
    ans_arr = []
    for i in range(len(iterable)):
        now = iterable[i]
        before = iterable[i-1]
        if (i == 0) or (now != before):
            ans_arr.append(now)
    return ans_arr
