#include <bits/stdc++.h>
using namespace std;

#define ll long long
int main()
{
    int n;
    cin >> n;
    int check = 0;
    ll ans = 0;
    for (int i=0; i < n; i++)
    {
        int num;
        cin >> num;
        check = max(check, num);
        ans += check-num;
    }
    cout << ans;
}
