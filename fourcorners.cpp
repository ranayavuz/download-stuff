#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));

    // Create a list of corners (1 to 4).
    int corners[] = {1, 2, 3, 4};

    // Display the corner choices
    cout << "Four corners\n";
    cout << "Choose a corner (1-4): ";
    
    int ans;
    cin >> ans;

    // Check if the answer is valid (between 1 and 4)
    if (ans < 1 || ans > 4) {
        cout << "Invalid choice. Please choose a number between 1 and 4.\n";
        return 1;
    }

    // Generate a random choice for the "winning" corner
    int winningCorner = corners[rand() % 4];

    // Check if the user's choice matches the winning corner
    if (ans == winningCorner) {
        cout << "you lost: " << ans << endl;
    } else {
        cout << "you won the corner is: " << winningCorner << endl;
    }

    return 0;
}
