#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define nl "\n"

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int l;
        cin >> l;
        vector<int> arr(l);

        for (int i=0; i<l; i++)
        {
            cin >> arr[i];
        }

        int ans = 0;
        sort(begin(arr), end(arr));
        for (int i=1; i<l; i++)
        {
            ans += arr[i];
        }
        cout << ans << nl;
    }

    return 0;
}
