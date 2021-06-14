// 20/100
#include<bits/stdc++.h>
using namespace std;
#define endl "\n"
vector<int> arr[500001];
int A[500001], B[500001], vkalitA[500001], vkalitB[500001];

// Declare def
void helper1 (int t_node, int dis)
{
    A[t_node] = 1;
    vkalitA[t_node] = dis;
    for(int child : arr[t_node])
    {
        if(A[child] == 0)
        {
            int helperhelper1 = vkalitA[t_node] + 1;
            helper1(child, helperhelper1);
        }
    }
}

// Declare def
void helper2 (int t_node, int dis)
{
    B[t_node] = 1;
    vkalitB[t_node] = dis;
    for(int child : arr[t_node])
    {
        if(B[child] == 0)
        {
            int helperhelper2 = vkalitB[t_node] + 1;
            helper2(child, helperhelper2);
        }
    }
}

int main()
{
    int t;
    cin>>t;
    // Declare while loop
    while(t--)
    {
        int n,a,b,q;
        cin>>n>>q;
        // Declare for loop
        for(int i=1;i<n;i++)
        {
            cin>>a>>b;
            arr[a].push_back(b);
            arr[b].push_back(a);
        }
        // Declare while loop
        while(q--)
        {
            int ans=0;
            cin>>a>>b;
            helper1(a,0);
            helper2(b,0);
            // Declare for loop
            for(int i=1; i<=n; i++)
            {
                ans += min(vkalitA[i],vkalitB[i]);
            }
            cout<<ans<<endl;

            // Declare for loop
            // Pengosongan array
            for(int j=1; j<=n; j++)
            {
                A[j] = 0; // Lakukan pengosongan pada array
                B[j] = 0; // Lakukan pengosongan pada array
                vkalitA[j] = 0; // Lakukan pengosongan pada array
                vkalitB[j] = 0; // Lakukan pengosongan pada array
            }
        }
        for(int k=1; k<=n; k++)
        {
            arr[k].clear();
            A[k] = 0; // Lakukan pengosongan pada array
            B[k] = 0; // Lakukan pengosongan pada array
            vkalitA[k] = 0; // Lakukan pengosongan pada array
            vkalitB[k] = 0; // Lakukan pengosongan pada array
        }
    }
    return 0;
}
