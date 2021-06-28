#include <stdio.h>
#define ull unsigned long long

int main()
{
    int t;
    scanf("%d", &t);
    getchar();
    while(t--)
    {
        ull a;
        ull b;
        scanf("%llu %llu", &a, &b);

        bool ans = true;

        while(b != 1)
        {
            if(b%2 == 1)
            {
                ans = false;
                break;
            }
            else
            {
                b /= 2;
            }
        }

        if(ans)
        {
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
        }
    }
}
