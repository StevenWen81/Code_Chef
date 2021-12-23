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

        sort(begin(arr), end(arr));
        int low = arr[0];
        int high =  arr[l-1];
        cout << high-low << nl;

    }

    return 0;
}
