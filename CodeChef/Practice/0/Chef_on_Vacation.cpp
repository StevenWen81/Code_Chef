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
        int x, y, z;
        cin >> x >> y >> z;
        if (x+y <= z)
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
