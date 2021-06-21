#include <bits/stdc++.h>
using namespace std;

#define ll long long
int main()
{
    ll n;
    ll total;
    ll check = 0;
    cin >> n;
    for (int i = 1; i<n; i++)
    {
        int num;
        cin >> num;
        check += num;
    }
    total = n * (n+1) / 2;
    cout << total-check;
}
