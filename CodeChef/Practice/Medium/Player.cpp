#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>

using namespace std;

#define nl '\n'

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int num;
        cin >> num;

        float ans = 0;
        for (int i=1; i<=num; i++)
        {
            ans += pow(i,-1);
        }
        ans *= num;

        cout << fixed;
        cout << setprecision(1);
        cout << ans << nl;
    }

    return 0;
}

