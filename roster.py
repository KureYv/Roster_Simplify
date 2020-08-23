import os
import json

print("Enter path of txt file to record roster and changes")
directory = input()
if (not os.path.isfile(directory)):
    print("There is no such file")
    exit()
print("File found")

def main():
    print("Add to roster history or delete history [add, delete]")
    decision = input()
    if (decision == "add"):
        output = open(directory,'a')
        for i in range(1,6):
            print("Player"+str(i))
            output.write(input() + ' ')
        output.write("\n")
    elif (decision == "delete"):
        delete = open(directory,'w')
        exit()

if __name__ == "__main__":
    main()
    exit()




        


