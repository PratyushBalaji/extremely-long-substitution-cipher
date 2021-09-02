# from functions import az, azAZ, azAZ123
def az():
    print()
    print("Avoid repeating characters")
    print()
    print("You have chosen the character set in order : ")
    print("abcdefghijklmnopqrstuvwxyz")
    print()
    sub = str(input("Enter the substitution key (26 characters) : "))
    if len(sub) == 26:
        transto = [t for t in sub]
        print()
        print()
        cd = input("Do you wish to cipher or decipher? (c/d) : ")
        if cd == "c":
            end=""
            cipher = input("Type in the text you wish to cipher : ").lower()
            for i in cipher:
                if i == 'a':
                    end = end+transto[0]
                elif i == 'b':
                    end = end+transto[1]
                elif i == 'c':
                    end = end+transto[2]
                elif i == 'd':
                    end = end+transto[3]    
                elif i == 'e':
                    end = end+transto[4]   
                elif i == 'f':
                    end = end+transto[5] 
                elif i == 'g':
                    end = end+transto[6]
                elif i == 'h':
                    end = end+transto[7]
                elif i == 'i':
                    end = end+transto[8]
                elif i == 'j':
                    end = end+transto[9]
                elif i == 'k':
                    end = end+transto[10]
                elif i == 'l':
                    end = end+transto[11]
                elif i == 'm':
                    end = end+transto[12]
                elif i == 'n':
                    end = end+transto[13]
                elif i == 'o':
                    end = end+transto[14]
                elif i == 'p':
                    end = end+transto[15]
                elif i == 'q':
                    end = end+transto[16]
                elif i == 'r':
                    end = end+transto[17]
                elif i == 's':
                    end = end+transto[18]
                elif i == 't':
                    end = end+transto[19]
                elif i == 'u':
                    end = end+transto[20]
                elif i == 'v':
                    end = end+transto[21]
                elif i == 'w':
                    end = end+transto[22]
                elif i == 'x':
                    end = end+transto[23]
                elif i == 'y':
                    end = end+transto[24]
                elif i == 'z':
                    end = end+transto[25]
                else:
                    end = end+i 
            print(end)
            print()
            print()
            again = input("Try another? (y/n) : ").lower()
            if again == 'y':program()
            elif again == 'n':print();input("Goodbye!");quit()
        elif cd == "d":
            end=""
            decipher = input("Type in the text you wish to decipher : ")
            for i in decipher:
                if i == transto[0]:
                    end = end+"a"
                elif i == transto[1]:
                    end = end+"b"
                elif i == transto[2]:
                    end = end+"c"
                elif i == transto[3]:
                    end = end+"d"
                elif i == transto[4]:
                    end = end+"e"
                elif i == transto[5]:
                    end = end+"f"
                elif i == transto[6]:
                    end = end+"g"
                elif i == transto[7]:
                    end = end+"h"
                elif i == transto[8]:
                    end = end+"i"
                elif i == transto[9]:
                    end = end+"j"
                elif i == transto[10]:
                    end = end+"k"
                elif i == transto[11]:
                    end = end+"l"
                elif i == transto[12]:
                    end = end+"m"
                elif i == transto[13]:
                    end = end+"n"
                elif i == transto[14]:
                    end = end+"o"
                elif i == transto[15]:
                    end = end+"p"
                elif i == transto[16]:
                    end = end+"q"
                elif i == transto[17]:
                    end = end+"r"
                elif i == transto[18]:
                    end = end+"s"
                elif i == transto[19]:
                    end = end+"t"
                elif i == transto[20]:
                    end = end+"u"
                elif i == transto[21]:
                    end = end+"v"
                elif i == transto[22]:
                    end = end+"w"
                elif i == transto[23]:
                    end = end+"x"
                elif i == transto[24]:
                    end = end+"y"
                elif i == transto[25]:
                    end = end+"z"
                else:
                    end = end+i 
            print(end)
            print()
            print()
            again = input("Try another? (y/n) : ").lower()
            if again == 'y':program()
            elif again == 'n':print();input("Goodbye!");quit()
    elif not len(sub) == 26:
        input("The key has to be *26* characters, special characters, or single-digit numbers long")
        print()
        az()

def azAZ():
    print()
    print("Avoid repeating characters")
    print()
    print("You have chosen the character set in order : ")
    print("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print()
    sub = str(input("Enter the substitution key (52 characters) : "))
    if len(sub) == 52:
        transto = [t for t in sub]
        print()
        print()
        cd = input("Do you wish to cipher or decipher? (c/d) : ")
        if cd == "c":
            end=""
            cipher = input("Type in the text you wish to cipher : ")
            for i in cipher:
                if i == 'a':
                    end = end+transto[0]
                elif i == 'b':
                    end = end+transto[1]
                elif i == 'c':
                    end = end+transto[2]
                elif i == 'd':
                    end = end+transto[3]    
                elif i == 'e':
                    end = end+transto[4]   
                elif i == 'f':
                    end = end+transto[5] 
                elif i == 'g':
                    end = end+transto[6]
                elif i == 'h':
                    end = end+transto[7]
                elif i == 'i':
                    end = end+transto[8]
                elif i == 'j':
                    end = end+transto[9]
                elif i == 'k':
                    end = end+transto[10]
                elif i == 'l':
                    end = end+transto[11]
                elif i == 'm':
                    end = end+transto[12]
                elif i == 'n':
                    end = end+transto[13]
                elif i == 'o':
                    end = end+transto[14]
                elif i == 'p':
                    end = end+transto[15]
                elif i == 'q':
                    end = end+transto[16]
                elif i == 'r':
                    end = end+transto[17]
                elif i == 's':
                    end = end+transto[18]
                elif i == 't':
                    end = end+transto[19]
                elif i == 'u':
                    end = end+transto[20]
                elif i == 'v':
                    end = end+transto[21]
                elif i == 'w':
                    end = end+transto[22]
                elif i == 'x':
                    end = end+transto[23]
                elif i == 'y':
                    end = end+transto[24]
                elif i == 'z':
                    end = end+transto[25]
                elif i == 'A':
                    end = end+transto[26]
                elif i == 'B':
                    end = end+transto[27]
                elif i == 'C':
                    end = end+transto[28]
                elif i == 'D':
                    end = end+transto[29]    
                elif i == 'E':
                    end = end+transto[30]   
                elif i == 'F':
                    end = end+transto[31] 
                elif i == 'G':
                    end = end+transto[32]
                elif i == 'H':
                    end = end+transto[33]
                elif i == 'I':
                    end = end+transto[34]
                elif i == 'J':
                    end = end+transto[35]
                elif i == 'K':
                    end = end+transto[36]
                elif i == 'L':
                    end = end+transto[37]
                elif i == 'M':
                    end = end+transto[38]
                elif i == 'N':
                    end = end+transto[39]
                elif i == 'O':
                    end = end+transto[40]
                elif i == 'P':
                    end = end+transto[41]
                elif i == 'Q':
                    end = end+transto[42]
                elif i == 'R':
                    end = end+transto[43]
                elif i == 'S':
                    end = end+transto[44]
                elif i == 'T':
                    end = end+transto[45]
                elif i == 'U':
                    end = end+transto[46]
                elif i == 'V':
                    end = end+transto[47]
                elif i == 'W':
                    end = end+transto[48]
                elif i == 'X':
                    end = end+transto[49]
                elif i == 'Y':
                    end = end+transto[50]
                elif i == 'Z':
                    end = end+transto[51]
                else:
                    end = end+i 
            print(end)
            print()
            print()
            again = input("Try another? (y/n) : ").lower()
            if again == 'y':program()
            elif again == 'n':print();input("Goodbye!");quit()
        elif cd == "d":
            end=""
            decipher = input("Type in the text you wish to decipher : ")
            for i in decipher:
                if i == transto[0]:
                    end = end+"a"
                elif i == transto[1]:
                    end = end+"b"
                elif i == transto[2]:
                    end = end+"c"
                elif i == transto[3]:
                    end = end+"d"
                elif i == transto[4]:
                    end = end+"e"
                elif i == transto[5]:
                    end = end+"f"
                elif i == transto[6]:
                    end = end+"g"
                elif i == transto[7]:
                    end = end+"h"
                elif i == transto[8]:
                    end = end+"i"
                elif i == transto[9]:
                    end = end+"j"
                elif i == transto[10]:
                    end = end+"k"
                elif i == transto[11]:
                    end = end+"l"
                elif i == transto[12]:
                    end = end+"m"
                elif i == transto[13]:
                    end = end+"n"
                elif i == transto[14]:
                    end = end+"o"
                elif i == transto[15]:
                    end = end+"p"
                elif i == transto[16]:
                    end = end+"q"
                elif i == transto[17]:
                    end = end+"r"
                elif i == transto[18]:
                    end = end+"s"
                elif i == transto[19]:
                    end = end+"t"
                elif i == transto[20]:
                    end = end+"u"
                elif i == transto[21]:
                    end = end+"v"
                elif i == transto[22]:
                    end = end+"w"
                elif i == transto[23]:
                    end = end+"x"
                elif i == transto[24]:
                    end = end+"y"
                elif i == transto[25]:
                    end = end+"z"
                elif i == transto[26]:
                    end = end+"A"
                elif i == transto[27]:
                    end = end+"B"
                elif i == transto[28]:
                    end = end+"C"
                elif i == transto[29]:
                    end = end+"D"
                elif i == transto[30]:
                    end = end+"E"
                elif i == transto[31]:
                    end = end+"F"
                elif i == transto[32]:
                    end = end+"G"
                elif i == transto[33]:
                    end = end+"H"
                elif i == transto[34]:
                    end = end+"I"
                elif i == transto[35]:
                    end = end+"J"
                elif i == transto[36]:
                    end = end+"K"
                elif i == transto[37]:
                    end = end+"L"
                elif i == transto[38]:
                    end = end+"M"
                elif i == transto[39]:
                    end = end+"N"
                elif i == transto[40]:
                    end = end+"O"
                elif i == transto[41]:
                    end = end+"P"
                elif i == transto[42]:
                    end = end+"Q"
                elif i == transto[43]:
                    end = end+"R"
                elif i == transto[44]:
                    end = end+"S"
                elif i == transto[45]:
                    end = end+"T"
                elif i == transto[46]:
                    end = end+"U"
                elif i == transto[47]:
                    end = end+"V"
                elif i == transto[48]:
                    end = end+"W"
                elif i == transto[49]:
                    end = end+"X"
                elif i == transto[50]:
                    end = end+"Y"
                elif i == transto[51]:
                    end = end+"Z"
                else:
                    end = end+i 
            print(end)
            print()
            print()
            again = input("Try another? (y/n) : ").lower()
            if again == 'y':program()
            elif again == 'n':print();input("Goodbye!");quit()
    elif not len(sub) == 26:
        input("The key has to be *52* characters, special characters, or single-digit numbers long")
        print()
        azAZ()

def azAZ123():
    print()
    print("Avoid repeating characters")
    print()
    print("You have chosen the character set in order : ")
    print("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    print()
    sub = str(input("Enter the substitution key (62 characters) : "))
    if len(sub) == 62:
        transto = [t for t in sub]
        print()
        print()
        cd = input("Do you wish to cipher or decipher? (c/d) : ")
        if cd == "c":
            end=""
            cipher = input("Type in the text you wish to cipher : ")
            for i in cipher:
                if i == 'a':
                    end = end+transto[0]
                elif i == 'b':
                    end = end+transto[1]
                elif i == 'c':
                    end = end+transto[2]
                elif i == 'd':
                    end = end+transto[3]    
                elif i == 'e':
                    end = end+transto[4]   
                elif i == 'f':
                    end = end+transto[5] 
                elif i == 'g':
                    end = end+transto[6]
                elif i == 'h':
                    end = end+transto[7]
                elif i == 'i':
                    end = end+transto[8]
                elif i == 'j':
                    end = end+transto[9]
                elif i == 'k':
                    end = end+transto[10]
                elif i == 'l':
                    end = end+transto[11]
                elif i == 'm':
                    end = end+transto[12]
                elif i == 'n':
                    end = end+transto[13]
                elif i == 'o':
                    end = end+transto[14]
                elif i == 'p':
                    end = end+transto[15]
                elif i == 'q':
                    end = end+transto[16]
                elif i == 'r':
                    end = end+transto[17]
                elif i == 's':
                    end = end+transto[18]
                elif i == 't':
                    end = end+transto[19]
                elif i == 'u':
                    end = end+transto[20]
                elif i == 'v':
                    end = end+transto[21]
                elif i == 'w':
                    end = end+transto[22]
                elif i == 'x':
                    end = end+transto[23]
                elif i == 'y':
                    end = end+transto[24]
                elif i == 'z':
                    end = end+transto[25]
                elif i == 'A':
                    end = end+transto[26]
                elif i == 'B':
                    end = end+transto[27]
                elif i == 'C':
                    end = end+transto[28]
                elif i == 'D':
                    end = end+transto[29]    
                elif i == 'E':
                    end = end+transto[30]   
                elif i == 'F':
                    end = end+transto[31] 
                elif i == 'G':
                    end = end+transto[32]
                elif i == 'H':
                    end = end+transto[33]
                elif i == 'I':
                    end = end+transto[34]
                elif i == 'J':
                    end = end+transto[35]
                elif i == 'K':
                    end = end+transto[36]
                elif i == 'L':
                    end = end+transto[37]
                elif i == 'M':
                    end = end+transto[38]
                elif i == 'N':
                    end = end+transto[39]
                elif i == 'O':
                    end = end+transto[40]
                elif i == 'P':
                    end = end+transto[41]
                elif i == 'Q':
                    end = end+transto[42]
                elif i == 'R':
                    end = end+transto[43]
                elif i == 'S':
                    end = end+transto[44]
                elif i == 'T':
                    end = end+transto[45]
                elif i == 'U':
                    end = end+transto[46]
                elif i == 'V':
                    end = end+transto[47]
                elif i == 'W':
                    end = end+transto[48]
                elif i == 'X':
                    end = end+transto[49]
                elif i == 'Y':
                    end = end+transto[50]
                elif i == 'Z':
                    end = end+transto[51]
                elif i == '1':
                    end = end+transto[52]
                elif i == '2':
                    end = end+transto[53]
                elif i == '3':
                    end = end+transto[54]
                elif i == '4':
                    end = end+transto[55]
                elif i == '5':
                    end = end+transto[56]
                elif i == '6':
                    end = end+transto[57]
                elif i == '7':
                    end = end+transto[58]
                elif i == '8':
                    end = end+transto[59]
                elif i == '9':
                    end = end+transto[60]
                elif i == '0':
                    end = end+transto[61]
                else:
                    end = end+i 
            print(end)
            print()
            print()
            again = input("Try another? (y/n) : ").lower()
            if again == 'y':program()
            elif again == 'n':print();input("Goodbye!");quit()
        elif cd == "d":
            end=""
            decipher = input("Type in the text you wish to decipher : ")
            for i in decipher:
                if i == transto[0]:
                    end = end+"a"
                elif i == transto[1]:
                    end = end+"b"
                elif i == transto[2]:
                    end = end+"c"
                elif i == transto[3]:
                    end = end+"d"
                elif i == transto[4]:
                    end = end+"e"
                elif i == transto[5]:
                    end = end+"f"
                elif i == transto[6]:
                    end = end+"g"
                elif i == transto[7]:
                    end = end+"h"
                elif i == transto[8]:
                    end = end+"i"
                elif i == transto[9]:
                    end = end+"j"
                elif i == transto[10]:
                    end = end+"k"
                elif i == transto[11]:
                    end = end+"l"
                elif i == transto[12]:
                    end = end+"m"
                elif i == transto[13]:
                    end = end+"n"
                elif i == transto[14]:
                    end = end+"o"
                elif i == transto[15]:
                    end = end+"p"
                elif i == transto[16]:
                    end = end+"q"
                elif i == transto[17]:
                    end = end+"r"
                elif i == transto[18]:
                    end = end+"s"
                elif i == transto[19]:
                    end = end+"t"
                elif i == transto[20]:
                    end = end+"u"
                elif i == transto[21]:
                    end = end+"v"
                elif i == transto[22]:
                    end = end+"w"
                elif i == transto[23]:
                    end = end+"x"
                elif i == transto[24]:
                    end = end+"y"
                elif i == transto[25]:
                    end = end+"z"
                elif i == transto[26]:
                    end = end+"A"
                elif i == transto[27]:
                    end = end+"B"
                elif i == transto[28]:
                    end = end+"C"
                elif i == transto[29]:
                    end = end+"D"
                elif i == transto[30]:
                    end = end+"E"
                elif i == transto[31]:
                    end = end+"F"
                elif i == transto[32]:
                    end = end+"G"
                elif i == transto[33]:
                    end = end+"H"
                elif i == transto[34]:
                    end = end+"I"
                elif i == transto[35]:
                    end = end+"J"
                elif i == transto[36]:
                    end = end+"K"
                elif i == transto[37]:
                    end = end+"L"
                elif i == transto[38]:
                    end = end+"M"
                elif i == transto[39]:
                    end = end+"N"
                elif i == transto[40]:
                    end = end+"O"
                elif i == transto[41]:
                    end = end+"P"
                elif i == transto[42]:
                    end = end+"Q"
                elif i == transto[43]:
                    end = end+"R"
                elif i == transto[44]:
                    end = end+"S"
                elif i == transto[45]:
                    end = end+"T"
                elif i == transto[46]:
                    end = end+"U"
                elif i == transto[47]:
                    end = end+"V"
                elif i == transto[48]:
                    end = end+"W"
                elif i == transto[49]:
                    end = end+"X"
                elif i == transto[50]:
                    end = end+"Y"
                elif i == transto[51]:
                    end = end+"Z"
                elif i == transto[52]:
                    end = end+'1'
                elif i == transto[53]:
                    end = end+'2'
                elif i == transto[54]:
                    end = end+'3'
                elif i == transto[55]:
                    end = end+'4'
                elif i == transto[56]:
                    end = end+'5'
                elif i == transto[57]:
                    end = end+'6'
                elif i == transto[58]:
                    end = end+'7'
                elif i == transto[59]:
                    end = end+'8'
                elif i == transto[60]:
                    end = end+'9'
                elif i == transto[61]:
                    end = end+'0'
                else:
                    end = end+i 
            print(end)
            print()
            print()
            again = input("Try another? (y/n) : ").lower()
            if again == 'y':program()
            elif again == 'n':print();input("Goodbye!");quit()
    elif not len(sub) == 26:
        input("The key has to be *52* characters, special characters, or single-digit numbers long")
        print()
        azAZ123()

#end
#ciphers
intro = input("Do you want a brief introduction to substitution ciphers? (y/n) : ")
if intro == 'y':
    input("After every '//', Press 'enter' to move onto the next line //")
    print()
    input("This is a program to cipher or decipher substitution ciphers //")
    print()
    input("Substitution ciphers use a key to replace each character in plaintext with the corresponding character from the key //")
    print()
    input("If a key for 'abcd' is '1234', the plaintext 'babacdb' will be ciphered as '2121342' //")
    print()
    input("With the same key, if the ciphertext was '124123421', the plaintext would be 'abdabcdba' //")
    print()
    input("When creating a key, it is better not to reuse characters as this particular program systematically checks for characters //")
    input("This means that if it finds a single match, it will log that as the correct decipher //")
    input("Hence, if multiple letters have the same substitute, ciphering and deciphering may not return the original message //")
    print()
    input("This program also doesn't cipher numbers, punctuation marks, special characters, etc so those will stay the same //")
    print()
    input("Now that the intro is over, start using the program! //")
    print()
    print()
    print()
else:
    print()
    print()
    print()

def program():
    def selection():        
        print()
        print()
        print("1) a-z (lowercase)")
        print("2) a-z, A-Z (all cases)")
        print("3) a-z, A-Z, 0-9")
        select = int(input("Type in the corresponding number : "))
        if select == 1:
            az()
        elif select == 2:
            azAZ()
        elif select == 3:
            azAZ123()
        else:
            print()
            print("Type in a valid input (1,2,3) ")
            print()
            selection()
    selection()
program()
        
