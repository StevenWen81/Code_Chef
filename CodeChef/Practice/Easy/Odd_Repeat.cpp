#include <iostream>
#include <string>

using namespace std;

#define nl '\n'

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int n, k, s;
        cin >> n >> k >> s;
        cout << (s-n*n)/(k-1) << nl;
    }

    return 0;
}
