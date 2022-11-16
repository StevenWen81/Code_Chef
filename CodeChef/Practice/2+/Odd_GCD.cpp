#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

#define nl '\n'

int gcd(int a, int b)
{
    if (a==0)
        return b;
    return gcd(b%a, a);
}

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

        int start = arr[0];

        for (int i:arr)
        {
            start = gcd(start,i);
        }

        int cnt = 0;

        while (start%2==0)
        {
            cnt += 1;
            start /= 2;
        }

        cout << cnt << nl;
    }

    return 0;
}
