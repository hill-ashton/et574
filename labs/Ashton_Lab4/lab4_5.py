#lab4_5
#Ashton Hill

#There is no data at index 3, change it to 2 in order to print the last of 3 items. Index starts at 0
myInfo = ['apple','banana','cherry'] 
print(myInfo[2]) 

#In order to copy a list you must use list() to make sure you are not just assigning to a new variable
myInfo = ['apple','banana','cherry'] 
newInfo = list(myInfo)

#myInfo was made as a string var, in order to use [] the variable must be made as a list.
myInfo = ['s','e','a']    
myInfo[0] = 'p'   #Change the first letter from ‘s’ to ‘p’ 
print(myInfo)     #Print the value

#In order to use slicing to print reverse you must do ::-1
myInfo = [1, "two", 'three', 4]  
print(myInfo[::-1])

#Incorrect variable was used in second line, and .join() function only works with strings
myInfo = ['1', "two", 'three', '4']  
print(" <<<< ".join(myInfo))