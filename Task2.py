while True:
    while True:
        #this loop to return score and list to defult and make option to start game or end game
        list_of_number_choosen_first_player=[]
        list_of_number_choosen_secound_player=[]
        list_of_the_number=["1",'2','3','4','5','6','7','8','9']
        check_1_p1=0
        check_2_p1=0
        check_3_p1=0
        check_4_p1=0
        check_1_p2=0
        check_2_p2=0
        check_3_p2=0
        check_4_p2=0
        print("A)Start new game")
        print("B)exit game")
        option_to_control_the_Game=input("Please insert a valid choise: ")
        if  option_to_control_the_Game not in ["A","a",'b','B']:
            print("Please choose a valid choise")
            continue
        else :
            break
    if option_to_control_the_Game=="b" or option_to_control_the_Game=="B":
        break
    if option_to_control_the_Game=="a" or option_to_control_the_Game=="A":
        for i in range(0,4) :
            remaining_number=' '.join(list_of_the_number)
            print('Remaining numbers is '+remaining_number)
            while True :
                the_number_of_the_first_player=str(input("Player 1 choose a number: "))
                if  the_number_of_the_first_player not in list_of_the_number:
                    print("The number not exist")
                    print("Please enter number from the remaining list")
                    print(remaining_number)
                    continue
                else:
                    break  
            list_of_number_choosen_first_player.append(the_number_of_the_first_player)
            length_of_the_list_1=len(list_of_number_choosen_first_player)
            if length_of_the_list_1 == 3 :
                check_1_p1=int(list_of_number_choosen_first_player[0])+int(list_of_number_choosen_first_player[1])+int(list_of_number_choosen_first_player[2])
            if check_1_p1 == 15 :
                print("The number choosed by player 1: "+" ".join(list_of_number_choosen_first_player))
                print("The number choosed by player 2: "+" ".join(list_of_number_choosen_secound_player))
                print('Player 1 is the winner')

            if length_of_the_list_1 == 4 :
                check_2_p1=int(list_of_number_choosen_first_player[1])+int(list_of_number_choosen_first_player[2])+int(list_of_number_choosen_first_player[3])
                check_3_p1=int(list_of_number_choosen_first_player[0])+int(list_of_number_choosen_first_player[1])+int(list_of_number_choosen_first_player[3])
                check_4_p1=int(list_of_number_choosen_first_player[0])+int(list_of_number_choosen_first_player[2])+int(list_of_number_choosen_first_player[3])
            if check_2_p1==15 or check_3_p1==15 or check_4_p1==15:
                print("The number choosed by player 1: "+" ".join(list_of_number_choosen_first_player))
                print("The number choosed by player 2: "+" ".join(list_of_number_choosen_secound_player))
                print('Player 1 is the winner')
                break
            list_of_the_number.remove(str(the_number_of_the_first_player))
            remaining_number=' '.join(list_of_the_number)
            print('Remaining numbers is '+remaining_number)
            while True:
                the_number_of_the_secound_player=str(input("Player 2 choose a number: "))
                if  the_number_of_the_secound_player not in list_of_the_number:
                    print("The number not exist")
                    print("Please enter number from the remaining list")
                    print(remaining_number)
                    continue
                else:
                    break
            list_of_number_choosen_secound_player.append(the_number_of_the_secound_player)
            length_of_the_list_2=len(list_of_number_choosen_secound_player)
            check2=0
            if length_of_the_list_2 == 3 :
                check_1_p2=int(list_of_number_choosen_secound_player[1])+int(list_of_number_choosen_secound_player[0])+int(list_of_number_choosen_secound_player[2])
            if check_1_p2==15:
                print("The number choosed by player 1: "+" ".join(list_of_number_choosen_first_player))
                print("The number choosed by player 2: "+" ".join(list_of_number_choosen_secound_player))
                print("Player 2 is the winner")
                break
            if length_of_the_list_2 == 4 :
                check_2_p2=int(list_of_number_choosen_secound_player[1])+int(list_of_number_choosen_secound_player[3])+int(list_of_number_choosen_secound_player[2])
                check_3_p2=int(list_of_number_choosen_secound_player[0])+int(list_of_number_choosen_secound_player[1])+int(list_of_number_choosen_secound_player[3])
                check_4_p2=int(list_of_number_choosen_secound_player[0])+int(list_of_number_choosen_secound_player[2])+int(list_of_number_choosen_secound_player[3])
            if check_2_p2==15 or check_3_p2==15 or check_4_p2==15:
                print("The number choosed by player 1: "+" ".join(list_of_number_choosen_first_player))
                print("The number choosed by player 2: "+" ".join(list_of_number_choosen_secound_player))
                print("Player 2 is the winner")
                break
            list_of_the_number.remove(str(the_number_of_the_secound_player))
            if i==3:
                    print("The number choosed by player 1: "+" ".join(list_of_number_choosen_first_player))
                    print("The number choosed by player 2: "+" ".join(list_of_number_choosen_secound_player))
                    print("The game is draw")