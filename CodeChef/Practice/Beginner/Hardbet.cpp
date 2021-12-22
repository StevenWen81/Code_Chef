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
        int a, b, c;
        cin >> a >> b >> c;

        if (b<=a && b<=c)
        {
            cout << "Bob" << nl;
        }
        else if (c<=a && c<=b)
        {
            cout << "Alice" << nl;
        }
        else
        {
            cout << "Draw" << nl;
        }
    }

    return 0;
}
