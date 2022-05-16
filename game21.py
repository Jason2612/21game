import random


while True:
    current_number = 0
    current_player = random.randint(0, 1)
    while current_number <= 21:
        print("Tong so hien tai" + " " + str(current_number))
        if current_player == 0:
            print("Human")
            player_choice = int(input("Nhap gia tri 1, 2 hoac 3: "))
            number_list = [1, 2, 3]
            while player_choice in number_list:
                current_number += player_choice
                break
            else:
                player_choice = int(input("Nhap gia tri 1, 2 hoac 3: "))

            current_player == 1

            if current_number >= 21:
                print("Human lost " + str(current_number))
                break
            else:
                current_player == 1
                print("Computer")
                computer_choice = random.randint(1, 3)
                print(computer_choice)
                current_number += computer_choice
                if current_number >= 21:
                    print("Human won " + str(current_number))
                    break
                else:
                    current_player == 0
        elif current_player == 1:
            print("Computer")
            computer_choice = random.randint(1, 3)
            print(computer_choice)
            current_number += computer_choice
            print("Tong so hien tai" + " " + str(current_number))
            if current_number >= 21:
                print("Human won " + str(current_number))
                break
            else:
                current_player == 0
                print("Human")
                player_choice = int(input("Nhap gia tri 1, 2 hoac 3: "))
                number_list = [1, 2, 3]
                while player_choice in number_list:
                    current_number += player_choice
                    break
                else:
                    player_choice = int(input("Nhap gia tri 1, 2 hoac 3: "))
    play_again = input("De choi lay hay an y/ De ket thuc an n: ")
    if play_again == "y":
        continue
    elif play_again == "n":
        break

   

        
        

