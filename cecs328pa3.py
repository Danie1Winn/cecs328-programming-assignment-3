def max_profit(n, W, U, values, weights, volumes):
    # 2D DP tables for max profits (W * U)
    dp = [[0 * (U + 1) for _ in range(U + 1)] for _ in range(W + 1)]

    # keeps track of items chosen
    # keeps = True when the item is chosen
    keeps = [[[False for _ in range(U + 1)] for _ in range(W + 1)] for _ in range(n)]

    for i in range(n):
        wt, vol, val = weights[i], volumes[i], values[i]
        # iterate backwards preventing using the same item twice
        for w in range(W, wt - 1, -1):
            for v in range(U, vol - 1, -1):
                if dp[w - wt][v - vol] + val > dp[w][v]:
                    dp[w][v] = dp[w - wt][v - vol] + val
                    keeps[i][w][v] = True

    # backrack with keeps table
    chosen_indices = []
    curr_w, curr_v = W, U
    for i in range(n - 1, -1, -1):
        if keeps[i][curr_w][curr_v]:
            chosen_indices.append(i)
            curr_w -= weights[i]
            curr_v -= volumes[i]

    #sorts indices in increasing order
    chosen_indices.sort()

    # returns the final tuple (best_value, chosen_indices)
    return(dp[W][U], chosen_indices)