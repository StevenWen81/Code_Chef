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
        int l, h;
        cin >> l >> h;
        int ans = 0;

        while(l--)
        {
            int num;
            cin >> num;
            if (num>h)
            {
                ans += 1;
            }
        }
        cout << ans << nl;
    }

    return 0;
}
