#include <stdio.h>
#include <stdlib.h>

int    main()
{
    int n, min, max;
    int *input;
    
    scanf("%d", &n);
    input = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
        scanf("%d", &input[i]);
    min = input[0];
    max = input[0];
    for (int i = 1; i < n; i++)
    {
        if (min > input[i])
            min = input[i];
        if (max < input[i])
            max = input[i];
    }
    printf("%d", min * max);
    free(input);
    return (0);
}
