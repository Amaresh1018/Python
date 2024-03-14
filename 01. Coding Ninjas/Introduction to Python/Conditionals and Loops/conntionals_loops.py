'''
Problem statement
Given an integer n, find if n is positive, negative or 0.

If n is positive, print "Positive"
If n is negative, print "Negative"
And if n is equal to 0, print "Zero".

Constraints :
-100 <= n <= 100
'''

# def typeInteger(n):
#     if n>0:
#         return 'Positive'
#     elif n<0:
#         return "Negative"
#     return 'Zero'
# n = int(input())
# print(typeInteger(n))


'''
Problem statement
What will the following code segment print?

if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
       print('B')
    else:
      print('C')
else:
     print('D')

ans = B
'''


'''
Problem statement
Given an integer n, find and print the sum of numbers from 1 to n.

Note
Use while loop only.
'''

# def sumof_N_NaturalNumbers(n):
#     sum = 0

#     # i = 1
#     # while i <= n:
#     #     sum += i
#     #     i += 1
#     for i in range(1,n+1):
#         sum += i    
#     return sum

# n = int(input())
# print(sumof_N_NaturalNumbers(n))

'''
Problem statement
Given a number N, print sum of all even numbers from 1 to N.
'''

# def sum_all_even_numbers(n):
#     sum = 0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum += i
#     return sum
# n = int(input())
# print(sum_all_even_numbers(n))

'''
Problem statement
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
you need to convert all Fahrenheit values from Start to End at the gap of W, 
into their corresponding Celsius values and print the table.

Hint : Use type casting

Constraints :
0 <= S <= 90
S <= E <=  900
0 <= W <= 80 
'''

s = int(input())
e = int(input())
w = int(input())

for i in range(s,e+1,w):
    cel_val = (5/9)*(i-32)
    print(str(i) + ' ' + str(int(cel_val)))
