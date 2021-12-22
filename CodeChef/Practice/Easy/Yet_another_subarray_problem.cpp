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
        int num;
        cin >> num;
        for (int i=1; i<=num; i++)
        {
            cout << (i<<1) << " ";
        }
        cout << nl;
    }

	return 0;
}
