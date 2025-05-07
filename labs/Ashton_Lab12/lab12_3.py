#lab12_3
#ashton hill

def main():
    try:
        from lab12_3mod import makePresidentFile, appendPresidentFile, displayFile
        presidents = ["James Madison", "James Monroe", "John Quincy Adams"]
        
        makePresidentFile()
        appendPresidentFile(presidents)
        displayFile()

    except ImportError:
        print("The imported module does not exist.")
    except FileNotFoundError:
        print("The file you are trying to display does not exist")

main()