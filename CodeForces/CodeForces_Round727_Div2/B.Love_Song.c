#include <stdio.h>
#include <string.h>

int main()
{
    int len;
    int t;
    scanf("%d %d", &len, &t);
    getchar();

    char str[len];
    int ans[len];

    scanf("%s", str);
    for(int i = 0; i < len; i++)
    {
        ans[i+1] = ans[i]+str[i]-'a'+1;
    }

    while(t--)
    {
        int start;
        int end;
        scanf("%d %d", &start, &end);
        long long final_ans = 0;
        final_ans = ans[end]-ans[start-1];
        printf("%lld\n", final_ans);
    }

}
