#include <iostream>
#include <string>

using namespace std;

#define nl "\n"

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int ind = 0;
        int eng = 0;
        int input;

        for (int i=0; i<5; i++)
        {
            cin >> input;
            if (input == 1)
            {
                ind += 1;
            }
            if (input == 2)
            {
                eng += 1;
            }
        }

        if (ind > eng)
        {
            cout << "INDIA" << nl;
        }
        else if (eng > ind)
        {
            cout << "ENGLAND" << nl;
        }
        else
        {
            cout << "DRAW" << nl;
        }
    }

    return 0;
}
