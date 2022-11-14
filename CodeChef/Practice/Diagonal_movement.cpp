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
        int x;
        int y;
        cin >> x >> y;

        if (abs(x-y)%2==0)
        {
            cout << "YES" << nl;
        }
        else
        {
            cout << "NO" << nl;
        }
    }

    return 0;
}
