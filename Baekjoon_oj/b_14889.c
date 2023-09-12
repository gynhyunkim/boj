#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int **team;
int *visited;
int min;

void count(int num, int cur, int n)
{
    if (cur == n / 2)
    {
        int start = 0;
        int link = 0;
        int balance = 0;
        for (int i = 0; i < n; i++)
        {
			for (int j = 0; j < n; j++)
			{
				if (visited[i] && visited[j])
					start += team[i][j];
				else if (!visited[i] && !visited[j])
					link += team[i][j];
			}   
        }
        balance = start > link ? start - link : link - start;
        min = min > balance ? balance : min;
        return ;
    }
    for (int i = num; i < n; i++)
    {
        visited[i] = 1;
        count(i + 1, cur + 1, n);
        visited[i] = 0;
    }
}

int main(void)
{
    int n;

    scanf("%d", &n);
    team = malloc(sizeof(int *) * n);
    visited = calloc(sizeof(int), n);
    for (int i = 0; i < n; i++)
        team[i] = malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			scanf("%d", &team[i][j]);			
	}
    min = INT_MAX;
    count(0, 0, n);
    printf("%d", min);
	for (int i = 0; i < n; i++)
        free(team[i]);
    free(team);
    free(visited);
    return (0);
}