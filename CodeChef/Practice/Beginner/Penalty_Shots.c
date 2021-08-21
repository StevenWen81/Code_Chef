#include <stdio.h>

int main()
{
    int t;
    scanf("%d \n" , &t);

    while (t--)
    {
        int k1, k2, k3, k4, k5;
        int k6, k7, k8 ,k9 ,k10;

        scanf("%d %d %d %d %d", &k1, &k2, &k3, &k4, &k5);
        scanf("%d %d %d %d %d", &k6, &k7, &k8, &k9, &k10);

        int team1 = k1 + k3 + k5 + k7 + k9;
        int team2 = k2 + k4 + k6 + k8 + k10;

        if (team1 > team2)
        {
            printf("1 \n");
        }
        else
        {
            if (team1 == team2)
            {
                printf("0 \n");
            }
            else
            {
                printf("2 \n");
            }
        }
    }
    return 0;
}
