def max_profit(n, W, U, values, weights, volumes):
    # dp[i][w][v] stores max profit for first i items
    # (n + 1) * (W + 1) * (U + 1)
    dp = [[[0 for _ in range(U + 1)] for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_weight = weights[i - 1]
        item_volume = volumes[i - 1]
        item_value = values[i - 1]

        for w in range(W + 1):
            for v in range(U + 1):
                dp[i][w][v] = dp[i - 1][w][v] # ignores current item

                # if item fits, take it
                if w >= item_weight and v >= item_volume:
                    dp[i][w][v] = max(dp[i][w][v], 
                                      dp[i - 1]
                                      [w - item_weight]
                                      [v - item_volume]
                                      + item_value)


    return (0, []) # placeholder