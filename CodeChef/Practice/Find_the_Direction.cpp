#include <iostream>
#include <string>

using namespace std;

#define nl '\n'

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int sec;
        cin >> sec;
        sec %= 4;

        switch(sec)
        {
            case 0:
                cout << "North" << nl;
                break;
            case 1:
                cout << "East" << nl;
                break;
            case 2:
                cout << "South" << nl;
                break;
            case 3:
                cout << "West" << nl;
                break;
        }
    }

    return 0;
}
