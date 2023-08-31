'''
Write a code to get the input in the given format and print the output in the given format.

Input Description:
A single line contains three float values separated by space.

Output Description:
Print the float value separated by line.

Sample Input :
2.3 4.5 7.8
Sample Output :
2.3
4.5
7.8
'''
a=input()
for i in a.split(" "):
    print(i)