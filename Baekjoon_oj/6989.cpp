#include <bits/stdc++.h>
using namespace std;
const int N = 152;

int n, k, arr[N], sum[N], score[N][N];

bitset<1140000> DT[N];

void input() {
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> arr[i], sum[i] = sum[i - 1] + arr[i];
	for (int i = 1; i <= n; i++)
		for (int j = i; j <= n; j++)
			score[i][j] = score[i][j - 1] + sum[j] - sum[i - 1];
	cin >> k;
}

void solve() {
	// 배점의 총합이 k보다 작은 경우
	if (k > score[1][n]) {
		cout << k;
		return ;
	}
	// 전체 비트를 0으로 셋팅
	DT[0].set(0);
	// j부터 i까지 문제를 맞은 경우 
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i + 1; j++) {
			if (j <= 2)
				DT[i].set(score[j][i]);
			else
				DT[i] |= (DT[j - 2] << score[j][i]);
		}
	}
	int ans = k;
	while (DT[n].test(ans)) ans++;
	cout << ans;
}

int main() {
	input();
	solve();
	return 0;
}

