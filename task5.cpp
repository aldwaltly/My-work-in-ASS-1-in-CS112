// Program: Number scrabble
// Author: Youssef Mohamed Mohamed 20230511
// Version: V1.0
// Date: 3/1/2024





#include <iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main() {
	while (true){//this loop to return score and list to defult and make option to start game or end game
		int check1_p1 = 0, check2_p1 = 0, check3_p1 = 0, check4_p1 = 0;
		int check1_p2 = 0, check2_p2 = 0, check3_p2 = 0, check4_p2 = 0;
		vector<string> remaining_number = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };
		vector<string> list1_p1 = {};
		vector<string> list2_p2 = {};
		string p1_choose = "";
		string p2_choose = "";
		string choose1 = "";
		while (true) {//this loop to make validation for the main menu
			cout << "A)start new game" << endl << "B)exit game" << endl;
			cin >> choose1;
			if (choose1 != "A" && choose1 != "a" && choose1 != "B" && choose1 != "b") {
				cout << "\n" << "Please enter a valid choise" << endl;
				continue;//continue to return to the loop
			}
			else {
				break;//break to break the loop
			}
		}
		if (choose1 == "B" || choose1 == "b") {
			break;
		}
		else {
			for (int i = 0; i < 4; i++) {//four loops to make 4 round every round player 1 and 2 get a number
				while (true) {//this loop to make a validation to player 1
					cout << "remaining number is: ";
					for (const string& num : remaining_number) {//this is a way to convert from vector to string
						cout << num << " ";
					}
					cout << endl << "Player1: please enter a number from the remaining number" << endl;
					cin >> p1_choose;
					if (find(remaining_number.begin(), remaining_number.end(), p1_choose) == remaining_number.end()) {
						cout << "the number not exist" << endl;
						continue;
					}
					else break;
				}
				remove(remaining_number.begin(), remaining_number.end(),p1_choose);//thi line to remove the number that player 1 choosed from the remaining number
				list1_p1.push_back(p1_choose);//pushback its a function to increase vector size to add the number of player1 to his vector
				if (i == 2) {
					check1_p1 = stoi(list1_p1[0]) + stoi(list1_p1[1]) + stoi(list1_p1[2]);//stoi its function from library <string> to convert string to integer
				}
				if (i == 3) {
					check2_p1 = stoi(list1_p1[1]) + stoi(list1_p1[2]) + stoi(list1_p1[3]);
					check3_p1 = stoi(list1_p1[0]) + stoi(list1_p1[1]) + stoi(list1_p1[3]);
					check4_p1 = stoi(list1_p1[0]) + stoi(list1_p1[2]) + stoi(list1_p1[3]);//this is all  possible value u can get from summtion of 3 numbers from 4 numbers
				}
				if (check1_p1 == 15 || check2_p1 == 15 || check3_p1 == 15 || check4_p1 == 15) {//check this values and any value = 15 player 1 is the winner
					cout << "the number choosed by player 1: ";
					for (const string& num : list1_p1) {
						cout << num << " ";
					}
					cout << endl << "the number choosed by player 2: ";
					for (const string& num : list2_p2) {
						cout << num << " ";
					}
					cout << endl << "player 1 is the winner\a" << endl << endl;
					break;//then break the loop
					
				}
				while (true) {//same algorithm to player 2
					cout << "remaining number is: ";
					for (const string& num : remaining_number) {
						cout << num << " ";
					}
					cout << endl << "Player2: please enter number from the remaining number" << endl;
					cin >> p2_choose;
					if (find(remaining_number.begin(), remaining_number.end(), p2_choose) == remaining_number.end()) {
						cout << "the number not exist" << endl;
						continue;
					}
					else break;
				}
				remove(remaining_number.begin(), remaining_number.end(), p2_choose);
				list2_p2.push_back(p2_choose);
				if (i == 2) {
					check1_p2 = stoi(list2_p2[0]) + stoi(list2_p2[1]) + stoi(list2_p2[2]);
				}
				if (i == 3) {
					check2_p2 = stoi(list2_p2[1]) + stoi(list2_p2[2]) + stoi(list2_p2[3]);
					check3_p2 = stoi(list2_p2[0]) + stoi(list2_p2[1]) + stoi(list2_p2[3]);
					check4_p2 = stoi(list2_p2[0]) + stoi(list2_p2[2]) + stoi(list2_p2[3]);
				}
				if (check1_p2 == 15 || check2_p2 == 15 || check3_p2 == 15 || check4_p2 == 15) {
					cout << "the number choosed by player 1: ";
					for (const string& num : list1_p1) {
						cout << num << " ";
					}
					cout << endl << "the number choosed by player 2: ";
					for (const string& num : list2_p2) {
						cout << num << " ";
					}
					cout << endl << "player 2 is the winner\a" << endl << endl;
					break;
				}
				if (i==3) {//this condtion to print the game is draw in the last loop and the code dosent break
					cout << "the game is draw" << endl;
				}
			}
		}
	}
}