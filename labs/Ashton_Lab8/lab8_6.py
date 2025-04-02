#lab8_6
#Ashton Hill
def middle(l):
    n = []
    if len(l)>1:
        l.pop(0)
        l.pop(-1)
        for i in l:
            n.append(i)
        return n
    else:
        return l
#print(middle([1,2,3,4]))
def main():
    import random
    n = random.randint(1,10)
    numList = [i for i in range(1,n)]
    if(len(numList)==1):
        print("No change made to the list.")
    print(f"List length = {n-1}\n{numList}\n{middle(numList)}")

main()