#include<stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int x;
        int m;
        int d;
        scanf("%d %d %d", &x, &m, &d);
        int ans = x * m;
        if (ans > x+d)
        {
            ans = x + d;
        }
        printf("%d\n", ans);
    }
}
