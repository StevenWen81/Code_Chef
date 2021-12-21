#include <iostream>
#include <string>

using namespace std;

#define nl '\n'

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int num;
        cin >> num;

        if (num%2==0)
        {
            if ((num%4) == 2)
            {
                cout << "YES" << nl;
            }
            else
            {
                cout << "NO" << nl;
            }
        }
    }

    return 0;
}
