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
        int tot, cor, pass;
        cin >> tot >> cor >> pass;

        if (cor*3 - (tot-cor) >= pass)
        {
            cout << "PASS" << nl;
        }
        else
        {
            cout << "FAIL" << nl;
        }
    }

    return 0;
}
