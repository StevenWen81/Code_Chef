#include<stdio.h>

int main()
{
    int t;
    scanf("%d",&t);

    while (t--)
    {
        int s;
        int ans = 0;
        scanf("%d",&s);
        while (s--)
        {
            int x,y;
            scanf("%d %d", &x, &y);
            ans += x-y;
        }
        printf("%d \n", ans);
    }

    return 0;
}
