def the_process():
    new_word=''
    print("Please enter the word you want you encrypt it: ")
    the_word=input()
    while True:
        print("Please enter a number to shift between 1-25 (please enter only number)")
        shift=int(input())
        if shift in range(1,26): break
        else: continue
    lengthofword=len(the_word)
    for i in range (0,lengthofword):
        ascii=int(ord(the_word[i]))
        if ascii in range (65,91-shift):
            new_ascii=ascii+shift
            new_word+=str(chr(new_ascii))
        elif ascii in range (91-shift,91):
            ascii+=shift
            new_ascii=ascii-26
            new_word+=str(chr(new_ascii))
        elif ascii in range (97,123-shift):
            new_ascii=ascii+shift
            new_word+=str(chr(new_ascii))
        elif ascii in range (123-shift,123):
            ascii+=shift
            new_ascii=ascii-26
            new_word+=str(chr(new_ascii))
        else:
            new_word+=str(chr(ascii))
    print('The new word is:')
    print(new_word)

print("**********   welcome to the extreme encreption program   **********")
while True:
    while True:
        print("A) Start new encryption")
        print("B) Exit program")
        choise1=input('Please choose a valid choise: ')
        if choise1 not in ["A","a","B",'b']:
            print('Please enter a valid choise')
            continue
        else :
            break
    if choise1=="B"or choise1=="b":
        print("Thank you!")
        break
    if choise1=="A" or choise1=="a":
        the_process()