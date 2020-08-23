import os
import json

print("Enter path of txt file to record roster and changes")
directory = input()
if (not os.path.isfile(directory)):
    print("There is no such file")
    exit()
output = open(directory,'a')
print("File found")

def main():
    for i in range(1,6):
        print("Player"+str(i))
        output.write(input() + ' ')

if __name__ == "__main__":
    main()
    output.write("\n")




        


