##lab2_4 - Ashton Hill
#A - .upper is supposed to be within the (), and the 'u' is lowercase
print("Python".upper())

#B - in order to print the ' while using single quotes, backslash it
print('Say it aint\' so.')

#C - if there is no Hotel variable, quotes need to be around the text in order to print
print('*'*5 +"Hotel"+'*'*5)

#D - Cannot make variable name "class"; Must cast an int in order to concatenate.
txt = "ET"
Class = 574
print(txt+str(Class))

#E - to use the find function you must have a string. We can cast our int to fix.
n = 1234
print(str(n).find('2'))

#F - similar to E, you cannot index an int. can fix with casting the int. 
num = 101
print(str(num)[0])