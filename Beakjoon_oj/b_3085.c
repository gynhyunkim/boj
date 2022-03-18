#include <stdio.h>
#include <stdlib.h>
#define MAX(a, b) (((a) >= (b)) ? (a) : (b))

void	swap(char **c, int i1, int j1, int i2, int j2)
{
	char tmp;

	tmp = c[i1][j1];
	c[i1][j1] = c[i2][j2];
	c[i2][j2] = tmp;
}

int	check_max(char **c, int n, int max)
{
	int max_w = 0, max_h = 0;

	for (int i = 0; i < n; i++)
	{
		int cnt_w = 1, cnt_h = 1;
		for (int j = 1; j < n; j++)
		{
			if (c[i][j - 1] == c[i][j])
				cnt_w++;
			else
			{
				max_w = MAX(max_w, cnt_w);
				cnt_w = 1;
			}
			if (c[j - 1][i] == c[j][i])
				cnt_h++;
			else
			{
				max_h = MAX(max_h, cnt_h);
				cnt_h = 1;
			}
		}
		max_w = MAX(max_w, cnt_w);
		max_h = MAX(max_h, cnt_h);
	}
	return (MAX(MAX(max_w, max_h), max));
}

int change(char **c, int n)
{
	int i2, j2, max;

	max = check_max(c, n, 0);
	for (int i = 0; i < n; i++)
	{
		if (max == n - 1)
			return (max);
		for (int j = 0; j < n - 1; j++)
		{
			if (c[i][j] != c[i][j + 1])
			{
				swap(c, i, j, i, j + 1);
				max = check_max(c, n, max);
				swap(c, i, j, i, j + 1);
			}
			if (c[j][i] != c[j + 1][i])
			{
				swap(c, j, i, j + 1, i);
				max = check_max(c, n, max);
				swap(c, j, i, j + 1, i);
			}
		}
	}
	return (max);
}

int main(void)
{
    int n;
	int max;
    char **candy;
    
    scanf("%d", &n);
    candy = malloc(sizeof(char *) * n);
    for (int i = 0; i < n; i++)
    {
        candy[i] = malloc(n + 1);
        scanf("%s", candy[i]);
    }
	printf("%d", change(candy, n));
	for (int i = 0; i < n; i++)
        free(candy[i]);
	free(candy);
    return (0);
}