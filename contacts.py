import os
import time

def clear_screen():
    '''
        Clear the screen when called
    '''
    if os.name=="posix":
        os.system("clear")
    else:
        os.system("cls")

def main():
    '''
        The program logic
    '''

    #Check if the save file exits
    clear_screen()
    if os.path.exists("list.txt"):
        print("Checking file...")
        time.sleep(1)
    else:
        print("File does not exist")
        print("Creating file...")
        time.sleep(1)
        create_file=open("list.txt","w")
        create_file.close()
        
    #Read the save file
    tmp_file=open("list.txt","r")
    tmp=[]
    for line in tmp_file.readlines():
        tmp.append(line)
    tmp_file.close()

    #Print the contact list
    clear_screen()
    count=1
    print("Welcome to the contact list!\n")
    print("The list follows the stucture below:")
    print("Name, Phone number, Email\n")
    for line in tmp:
        print(count,line)
        count+=1

    #Take user command
    print("Commands: New Contact (N), Delete Contact (D), Update Contact (U), Exit (E)")

    command=input(">")

    if command=="N":
        #New Contact
        tmp_input=input("Enter contact details:")
        tmp.append(tmp_input+"\n")
    elif command=="D":
        #Delete Contact
        tmp_input=input("Enter contact id:")
        index=int(tmp_input)-1
        tmp.pop(index)
    elif command=="E":
        clear_screen()
        print("Bye!")
        return 0
    else:
        print("Error: Input must be a letter N, D, U or E")

    #Save data to file
    clear_screen()
    print("Saving data to file...")
    time.sleep(1)
    save_file=open("list.txt","w")
    write_tmp=""
    for line in tmp:
        write_tmp+=line
    save_file.write(write_tmp)
    save_file.close()

    main()

main()
