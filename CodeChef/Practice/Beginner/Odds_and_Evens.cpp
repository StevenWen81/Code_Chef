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

        cin >> a;
        cin >> b;

        int  tot;
        tot = a + b;

        if (tot%2==0)
        {
            cout << "Bob" << nl;
        }
        else
        {
            cout << "Alice" << nl;
        }
    }

    return 0;
}
