def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def mininum_coins_R(m, coins):
    memo = {}

    def _mininum_coins(m, coins):
        if m in memo:
            return memo[m]
        if m == 0:
            answer = 0
        else:
            answer = None
            for coin in coins:
                subproblem = m - coin
                if subproblem < 0:
                    # Skip solution where we try to reach [m]
                    # from a negative subproblem
                    continue
                answer = min_ignore_none(answer, _mininum_coins(subproblem, coins) + 1)

        memo[m] = answer
        return answer

    return _mininum_coins(m, coins)


def mininum_coins_iter(m, coins):
    memo = {}
    memo[0] = 0

    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)

    return memo[m]


def main():
    coins = [1, 4, 5]
    target_sum = 13
    print(mininum_coins_R(target_sum, coins))


if __name__ == "__main__":
    main()
