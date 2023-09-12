#include <stdio.h>
#include <stdlib.h>

void    pick(int *b, int *v, int *item, int n, int m, int i)
{
    int min;
   
    if (i == m)
    {
        for (int idx = 0; idx < m; idx++)
            printf("%d ", item[b[idx]]);
        printf("\n");
        return ;
    }
	min = i == 0 ? 0 : b[i - 1] + 1;
    for (int num = min; num < n; num++)
    {
		if (!v[num])
		{
			v[num] = 1;
        	b[i] = num;
        	pick(b, v, item, n, m, i + 1);
			v[num] = 0;
		}
	}
}

void	sort(int *arr, int n)
{
	int tmp;

	for (int i = 0; i < n - 1; i++)
	{
		for (int j = 0; j < n - 1; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}
}

int    main(void)
{
    int n, m;
    int *bucket;
	int *visited;
	int *item;
    
    scanf("%d %d", &n, &m);
    bucket = malloc(sizeof(int) * m);
	visited = calloc(sizeof(int), n);
	item = malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
		scanf("%d", &item[i]);
	sort(item, n);
    pick(bucket, visited, item, n, m, 0);
    free(bucket);
	free(visited);
	free(item);
    return (0);
}