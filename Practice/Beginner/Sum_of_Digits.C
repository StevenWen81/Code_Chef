#include<stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while(t--)
    {
        int num;
        scanf("%d", &num);

        int ans = 0;
        while (num>0)
        {
            ans += num%10;
            num /= 10;
        }
        printf("%d\n", ans);
    }
}
