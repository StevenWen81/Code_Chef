// 100/100
#include<bits/stdc++.h>
using namespace std;
#define int long long int
#define endl "\n"

// conditions need to check:
// m<a<b => count += 1
// a<b<m => no conclusion
// m=a<b => count += 1
// a<b=m => count += 0
// a<m<b => no conclusion

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t; 
    cin>>t;
    t = t + 1;
    while(t-=1)
    {
        int n, m; cin>>n>>m;
        int ans = 0;
        vector<int> mod(n+1,1);
        for(int a = 2;a<=n;a++) // assign loop
        {
            int jb = m%a;
            ans = ans + mod[jb];
            for(int b = jb;b<=n;b+=a) // assign loop
            {
                mod[b]++;
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}