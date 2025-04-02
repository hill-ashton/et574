#lab8_5
#Ashton Hill
def message(p1,p2):
    for i in range(0,p2):
        print(p1)
def main():
    import random 
    n = random.randint(1,10)
    text = input("Enter a text: ")
    print(f"text = {text}\nn = {n}\nmessage(text, n) will print the following:")
    message(text,n)

main()
    