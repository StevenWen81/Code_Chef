#include <iostream>
#include <string>

using namespace std;

#define nl "\n"

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int num;
        cin >> num;

        int ans = 1;
        switch(num)
        {
            case(1):
                cout << ans << nl;
                cout << ans << " " << ans << nl;
                break;
            case(2):
                ans += 1;
                cout << ans << nl;
                ans += 1;
                cout << ans << " " << ans-2 << nl;
                ans += 1;
                cout << ans << " " << ans-3 << nl;
                break;
            case(4):
                cout << ans << nl;
                ans += 1;
                cout << ans << " " << (ans<<1) << nl;
                break;
            default:
                ans += 1;
                num -= 1;
                cout << ans << nl;
                cout << ans << " " << num << nl;
                ans -= 1;
                num -= 1;
                cout << num << " " << ans << nl;
                break;
        }
    }

    return 0;
}
