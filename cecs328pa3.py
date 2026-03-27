def max_profit(n, W, U, values, weights, volumes):
    # dp[i][w][v] stores max profit for first i items
    # (n + 1) * (W + 1) * (U + 1)
    dp = [[[0 for _ in range(U + 1)] for _ in range(W + 1)] for _ in range(n + 1)]
    return (0, []) # placeholder