#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of each game based on the rules.

    Args:
        x (int): Number of rounds.
        nums (list): Array of n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None if tied.
    """
    if not nums or x < 1:
        return None

    # Precompute primes up to the maximum number in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Compute the cumulative count of primes up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve_of_eratosthenes(n):
    """
    Generate a list of primes up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The maximum number to check for primality.

    Returns:
        list: A list where index i is True if i is a prime number, otherwise False.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime
