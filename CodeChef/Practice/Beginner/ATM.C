#include<stdio.h>
int main()
{
    int take;
    float left;
    scanf("%d %f", &take, &left);

    if (take<left && take%5==0)
    {
        float ans = left - take;
        ans -=0.5;
        printf("%.2f", ans);
    }
    else
    {
        printf("%.2f", left);
    }
}
