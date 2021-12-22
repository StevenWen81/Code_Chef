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
        int n, l, x;
        cin >> n >> l >> x;

        if (n>= 2*l)
        {
            cout << l*x << nl;
        }
        else
        {
            cout << (n-l)*x << nl;
        }
    }

    return 0;
}
