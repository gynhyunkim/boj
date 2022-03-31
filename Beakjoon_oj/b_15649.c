#include <stdio.h>
#include <stdlib.h>

void    pick(int *b, int *v, int n, int m, int i)
{   
    if (i == m)
    {
        for (int idx = 0; idx < m; idx++)
            printf("%d ", b[idx]);
        printf("\n");
        return ;
    }
    for (int num = 1; num <= n; num++)
    {
		if (!v[num - 1])
		{
			v[num - 1] = 1;
        	b[i] = num;
        	pick(b, v, n, m, i + 1);
			v[num - 1] = 0;
		}
	}
}

int    main(void)
{
    int n, m;
    int *bucket;
	int *visited;
    
    scanf("%d %d", &n, &m);
    bucket = malloc(sizeof(int) * m);
	visited = calloc(sizeof(int), n);
	
    pick(bucket, visited, n, m, 0);
    free(bucket);
	free(visited);
    return (0);
}