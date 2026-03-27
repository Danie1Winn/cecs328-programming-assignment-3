def max_profit(n, W, U, values, weights, volumes):
    # 2D DP tables for max profits (W * U)
    dp = [[0 for _ in range(U + 1)] for _ in range(W + 1)]

    # keeps track of items chosen
    # keeps = True when the item is chosen
    keeps = [[[False for _ in range(U + 1)] for _ in range(W + 1)] for _ in range(n)]

    # iterate through each available item
    for i in range(n):
        curr_wt, curr_vol, curr_val = weights[i], volumes[i], values[i]


        # update DP table iterating backwards
        # critical for 2D DP tables to prevent overwriting
        for w in range(W, curr_wt - 1, -1):
            for v in range(U, curr_vol - 1, -1):

                # checks if profit is greater than current dp value
                # profit = (value curr item) + (max profit of remaining)
                if dp[w - curr_wt][v - curr_vol] + curr_val > dp[w][v]:
                    # updates max profit at the current capacity
                    dp[w][v] = dp[w - curr_wt][v - curr_vol] + curr_val
                    # mark item as kept
                    keeps[i][w][v] = True

    # backrack with keeps table
    chosen_indices = []
    rem_w, rem_v = W, U

    # start from last item, checks 'keeps' to see if it was chosen
    for i in range(n - 1, -1, -1):
        if keeps[i][rem_w][rem_v]:
            # when item is chosen, adds 0-based index to the list
            chosen_indices.append(i)
            # subtract item requirements from remaining
            rem_w -= weights[i]
            rem_v -= volumes[i]

    #sorts indices in increasing order
    chosen_indices.sort()

    # returns the final tuple (best_value, chosen_indices)
    return(dp[W][U], chosen_indices)