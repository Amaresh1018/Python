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


Q.2