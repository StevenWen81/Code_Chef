#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int ans = 0;
    int temp = 0;
    char l = 'A';
    for (char d:s)
    {
        //cout << d << endl;
        if (d==l)
        {
            temp += 1;
            ans = max(ans, temp);
        }
        else
        {
            l = d;
            temp = 1;
        }
    }
    cout << ans;
}
