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
        int a;
        int b;
        int c;

        cin >> a;
        cin >> b;
        cin >> c;

        if (a > (b*c))
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
