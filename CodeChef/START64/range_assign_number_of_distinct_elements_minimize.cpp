#include <iostream>
#include <vector>
using namespace std;

int main() {
    long loop;
    cin >> loop;
    
    while(loop--)
    {
        long n;
        cin >> n;
        
        vector<long> arr;
        arr.resize(n);
        
        
        long first = 0;
        long second = -1;
        long firstIdx;
        long secondIdx;
        bool flag = false;
        
        for(long i = 0; i < n; i++)
        {
            cin >> arr[i];
            
            if(i == 0)
                first = arr[i];
            if(arr[i] != arr[0] && second == -1)
            {
                second = arr[i];
            }
               
            if(arr[i] == first)
                firstIdx = i;
            if(arr[i] == second && second != -1)
            {
                secondIdx = i;
            }
        }
        
        for(long i = 0; i < n; i++)
        {
            if(arr[i-1] == first && arr[i] == arr[n-1])
            {
                flag = true;
            }
        }
        
        
        
        if(firstIdx == n-1)
        {
            flag = true;
        } 
        else if(second == -1)
        {
            flag = true;
        } 
        else if(secondIdx == n-1 )
        {
            flag = true;
        } 
        else if(arr[firstIdx+1] == arr[n-1])
        {
            flag = true;
        } 
        else if(arr[secondIdx] == arr[n-1])
        {
            flag = true;
        }
        
        if(flag)
        {
            cout << "YES\n";
        } 
        else 
        {
            cout << "NO\n";
        }
        
    }
    return 0;
}