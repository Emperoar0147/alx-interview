#!/usr/bin/python3

def sieve_of_eratosthenes(max_num):
    """
    Generate a list of prime numbers up to max_num using the Sieve of Eratosthenes.
    """
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    return primes

def calculate_wins(prime_flags, max_num):
    """
    Precompute the number of prime moves available up to each number.
    """
    moves = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if prime_flags[i]:
            count += 1
        moves[i] = count
    return moves

def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    
    Args:
        x: Number of rounds.
        nums: List of integers, where each integer is the upper bound for a round.
    
    Returns:
        Name of the player with the most wins, or None if tied.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    prime_flags = sieve_of_eratosthenes(max_num)
    prime_moves = calculate_wins(prime_flags, max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_moves[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
