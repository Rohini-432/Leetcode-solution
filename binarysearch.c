int numTrees(int n) {
    int dp[n + 1];
    for (int i = 0; i <= n; i++) {
        dp[i] = 0;
    }
    dp[0] = 1; 
    dp[1] = 1; 
    for (int nodes = 2; nodes <= n; nodes++) {
        for (int root = 1; root <= nodes; root++) {
            int left_nodes = root - 1;
            int right_nodes = nodes - root;
            dp[nodes] += dp[left_nodes] * dp[right_nodes];
        }
    }
    return dp[n];
}
