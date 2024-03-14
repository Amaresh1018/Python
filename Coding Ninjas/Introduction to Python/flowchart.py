'''
Q.1
You are given three numbers. You need to calculate and print their average value. 
Draw a flowchart for this process.

Note : You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.


+---------+            +--------+            +---------+
|         |            |        |            |         |
| Start   +----------->+ Input  +----------->+ Process |
|         |            |        |            |         |
+---------+            +--------+            +---------+
                          |   |                  |
                          |   +------------------+
                          |                      
                          v                      
                   +--------------+              
                   |    Output    |              
                   |              |              
                   +--------------+              
                          |                      
                          |                      
                          v                      
                   +--------------+              
                   |     End      |              
                   +--------------+   
'''

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average
average = (num1 + num2 + num3) / 3

# Print the average
print("The average of", num1, ",", num2, "and", num3, "is:", average)


'''
Q.2
You are given a single number. You need to print one of the following outputs according to the number's nature.

Print 1, if the number is positive

Print -1, if it's negative

Print 0, if it's equal to 0

Draw a flowchart for this process.

Note : You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.


+---------+            +--------+        +-----------+
|         |            |        |        |           |
| Start   +----------->+ Input  +------->+ Decision1 |
|         |            |        |        |           |
+---------+            +--------+        +-----------+
                          |   |  No             |
                          |   +-----------------+
                          |  Yes               |
                          v                     v
                   +-------------+       +-------------+
                   | Print 1     |       | Decision2   |
                   |             |       | (number < 0)|
                   +-------------+       +-------------+
                          |  No                  |
                          | Yes                  |
                          v                      v
                   +-------------+       +-------------+
                   | Decision3   |       | Print 0     |
                   | (number = 0)|       |             |
                   +-------------+       +-------------+
                          |                      |
                          +----------------------+
                                         
                          +                     
                   +-------------+       
                   |    End      |              
                   +-------------+   
'''

# Input a number from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(1)
elif number < 0:
    print(-1)
else:
    print(0)

'''
Q.3
You are given 3 numbers. Each number represents the length of a line. You need to figure out whether these lines can form a valid triangle.
If a valid triangle can be formed, print "Yes", otherwise print "No".

Draw a flowchart for this process

A triangle is a valid triangle, If and only If, the sum of any two sides of a triangle is greater than the third side. 
For Example, let A, B and C are three sides of a triangle. Then, A + B > C, B + C > A and C + A > B

Note : You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.

+---------+            +--------+        +-----------+
|         |            |        |        |           |
| Start   +----------->+ Input  +------->+ Decision  |
|         |            |        |        |           |
+---------+            +--------+        +-----------+
                          |   |  No             |
                          |   +-----------------+
                          |  Yes               |
                          v                     v
                   +-------------+       +-------------+
                   | Print "Yes" |       | Print "No" |
                   +-------------+       +-------------+
                                          
                          +                     
                   +-------------+       
                   |    End      |              
                   +-------------+   
'''

# Input lengths of three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the lengths can form a valid triangle
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
    print("Yes")
else:
    print("No")

'''
Q.4
You are given a single non-negative integer, N. You need to calculate and print N factorial (N!)

N factorial is defined as the product of all integers from 1 to N (both inclusive)

Draw a flowchart for this process

Note : You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.

+---------+            +--------+        +-----------+
|         |            |        |        |           |
| Start   +----------->+ Input  +------->+ Decision  |
|         |            |        |        |           |
+---------+            +--------+        +-----------+
                          |   |  Yes            |
                          |   +-----------------+
                          |  No               |
                          v                   v
                   +-------------+       +-------------+
                   | Print 1     |       | Process     |
                   +-------------+       |             |
                                         +-------------+
                                                   |
                                                   v
                                          +-------------+
                                          | Output      |
                                          | Print       |
                                          +-------------+
                          +                     
                   +-------------+       
                   |    End      |              
                   +-------------+   
'''

# Input N
N = int(input("Enter a non-negative integer: "))

# Check if N is 0 or 1
if N == 0 or N == 1:
    factorial = 1
else:
    factorial = 1
    for i in range(2, N + 1):
        factorial *= i

# Print factorial
print("Factorial of", N, "is:", factorial)

'''
Q.5
You are given a single positive integer, N. 
You need to print all even integers that occur between 1 and N (both inclusive).

Draw a flowchart for this process

Note : You don't need to submit the problem. 
       Just attempt in your notebook and ask doubts if you need help.

+---------+            +--------+        +-----------+
|         |            |        |        |           |
| Start   +----------->+ Input  +------->+ Process   |
|         |            |        |        |           |
+---------+            +--------+        +-----------+
                          |   |                  |
                          |   +------------------+
                          v                     |
                   +-------------+              |
                   | Decision    |              |
                   | (Is number  |              |
                   | even?)      |              |
                   +-------------+              |
                          |  No                  |
                          +----------------------+
                          |   Yes                |
                          v                      v
                   +-------------+       +-------------+
                   | Output      |       | End         |
                   | Print even  |       |             |
                   | number      |       +-------------+
                   +-------------+       
'''
# Input the positive integer N
N = int(input("Enter a positive integer: "))

# Loop from 1 to N
print("Even numbers between 1 and", N, "are:")
for num in range(1, N + 1):
    # Check if the current number is even
    if num % 2 == 0:
        print(num)
