#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);

    while(a--)
    {
        int x;
        int ans;
        scanf("%d", &x);
        if (2000 <= x)
        {
            ans = 1;
        }
        if (1600<=x && x<2000)
        {
            ans = 2;
        }
        if (x<1600)
        {
            ans = 3;
        }
        printf("%d \n", ans);
    }
}
