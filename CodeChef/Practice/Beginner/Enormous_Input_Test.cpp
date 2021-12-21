#include <iostream>
#include <string>
using namespace std;

#define  nl '\n'

int main()
{
    int t;
    int k;

    cin >> t;
    cin >> k;

    int num;
    int ans = 0;
    while (t--)
    {
        cin >> num;
        if (num%k==0)
        {
            ans += 1;
        }
    }
    cout << ans;

    return 0;
}
