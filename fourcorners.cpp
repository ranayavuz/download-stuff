#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main() {
  srand(time(0));
  int choice = rand() % 5;
cout << "four corners\n";
  cout << "choose a corner: ";
  int ans;
  cin >> ans;
  corners[4] = [1, 2, 3, 4];
  for(string i : corners) {
    if(!ans == i) {
      cout << "your cheating arent you?";
      cout << 1/0;
    }
  }
  
}
