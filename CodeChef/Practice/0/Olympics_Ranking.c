#include <stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int g1, s1, b1;
        int g2, s2, b2;
        scanf("%d %d %d", &g1, &s1, &b1);
        scanf("%d %d %d", &g2, &s2, &b2);

        int one = g1+s1+b1;
        int two = g2+s2+b2;

        if (one > two)
        {
            printf("1 \n");
        }
        else
        {
            printf("2 \n");
        }
    }


    return 0;
}
