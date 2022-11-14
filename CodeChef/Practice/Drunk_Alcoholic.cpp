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
        int step;
        cin >> step;
        if (step%2==0)
        {
            cout << step << nl;
        }
        else
        {
            cout << step+2 << nl;
        }
    }

    return 0;
}
