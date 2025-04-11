#lab9_5
#ashton hill
import random
def average(*grades):
    sum = 0
    for i in grades:
        sum+=i
    return(sum/len(grades))
def main():
    print(round(average(95,87,83,74),2))
    x, y, z = random.randint(-100,-1), random.randint(0,1), random.randint(1,100)
    print(round(average(x,y,z),2))

main()

#Having the ability to create my own functions when i program will enable me to make programs that can efficiently make use of different functions, like sorting or calculating. In addition, i can get extra flexibility by making a function accept an arbitrary number of values.
