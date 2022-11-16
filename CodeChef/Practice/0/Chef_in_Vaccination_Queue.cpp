#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define nl '\n'

int main()
{
    /// N => Queue length
    /// P-th => Chef position
    /// X => Time to vaccinate a child
    /// Y => Time to vaccinnate an elder
    /// 1 = elder; 0 = children

    int t;
    cin >> t;

    while(t--)
    {
        int n, p, x, y;
        int time = 0;

        cin >> n >> p >> x >> y;

        vector<int> arr(n);
        for (int i=0; i<n; i++)
        {
            cin >> arr[i];
        }

        for (int i=0; i<p; i++)
        {
            (arr[i] == 0) ? time+=x : time+=y;
        }

        cout << time << nl;
    }

    return 0;
}
