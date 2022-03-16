#include <stdio.h>
#include <stdlib.h>

int is_prime(int n)
{
    if (n == 1)
        return (0);
    for (int i = 2; i <= n / 2; i++)
        if (n % i == 0)
            return (0);
    return (1);
}

int main(void)
{
    int n, cnt;
    int *input;
    
    scanf("%d", &n);
    input = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
        scanf("%d", &input[i]);
    cnt = 0;
    for (int i = 0; i < n; i++)
        cnt += is_prime(input[i]);
    printf("%d", cnt);
    free(input);
    return (0);
}
