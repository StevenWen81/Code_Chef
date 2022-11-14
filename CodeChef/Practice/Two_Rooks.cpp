#include <iostream>
#include <string>

using namespace std;

#define nl "\n"

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int a,b, x,y;
        cin >> a >> b >> x >> y;
        if (a==x || b==y)
        {
            cout << "YES" << nl;
        }
        else
        {
            cout << "NO" << nl;
        }
    }

    return 0;
}
