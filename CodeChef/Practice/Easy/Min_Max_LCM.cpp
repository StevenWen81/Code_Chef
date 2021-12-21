#include <iostream>
#include <string>

using namespace std;

#define ll long long int
#define nl '\n'

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        ll x, k;
        cin >> x >> k;
        ll maks;
        maks = x*k;
        maks -= 1;
        maks *= x*k;
        cout << (x<<1) << " " << maks << nl;
    }

    return 0;
}
