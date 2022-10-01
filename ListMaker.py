import random,sys

username_chars = 'abcdefghijklmnopqrstuvwxyz1234567890-'
all_chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+}]{[\'";:/\\.,><`~QAZWSXEDCRFVTGBYHNUJMIKOLP'
LENGTH = input("Length : ")
HM = input("How Many : ")
isUsername = input("Username Format (Y/N): ").upper()
random_list = []
print("\n\n[-] Generating Random Wordlist, Please Wait...")



for i in range(int(HM)):
    rand = ''.join((random.choice(username_chars if isUsername == "Y" else all_chars) for i in range(int(LENGTH))))
    if isUsername == "Y":
        if rand[0] != "." and rand[-1] != ".":
            if rand not in random_list:
                random_list.append(rand)
        else:
            i -= 1
    else:
        random_list.append(rand)



print("\n[+] Wordlist Generated Successfully")
print("[!] Total Words: " + str(len(random_list)))
print("[-] Saving Wordlist, Please Wait...")
wordlist_file = open('list.txt', 'w')
for word in random_list:
    wordlist_file.write(word + "\n")
wordlist_file.close()
print("[+] File Saved As : wordlist.txt")
print("[+] Done !")
sys.exit()