#include <bits/stdc++.h>
using namespace std;

#define ll long long
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll x;
        ll y;
        cin >> y >> x;
        ll ans = 0;
        if (max(x,y)==x)
        {
            if (x%2==1)
            {
                ans = x*x - y + 1;
                cout << ans << "\n";
            }
            else
            {
                x -= 1;
                ans = x*x + y;
                cout << ans << "\n";
            }
        }
        else
        {
            if (y%2==0)
            {
                ans = y*y - x + 1;
                cout << ans << "\n";
            }
            else
            {
                y -= 1;
                ans = y*y + x;
                cout << ans << "\n";
            }
        }
    }
}
