#!/usr/bin/python3
""" 
Module for solving the prime game question.

The prime game involves determining the winner of a game played between two players, Maria and Ben. 
The game uses a list of numbers where each number represents the upper limit for a round.
The winner is determined based on the number of primes found up to each number in the rounds.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game based on the given rules.

    Args:
        x (int): Number of rounds to be played.
        nums (list of int): List of integers where each integer represents 
                            the upper limit for a round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
        None: If the game is tied or there are no valid rounds.

    Description:
        - Maria wins a round if the count of primes up to the given number is odd.
        - Ben wins if the count is even.
        - The function uses the Sieve of Eratosthenes to calculate prime numbers efficiently.
        - The player with the majority of wins across all rounds is declared the overall winner.

    Example:
        >>> isWinner(3, [4, 5, 1])
        'Ben'
    """
    if not nums or x < 1:
        return None

    # Determine the maximum number in the list for sieve computation
    max_num = max(nums)

    # Create a list to mark prime numbers using Sieve of Eratosthenes
    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False

    # Mark 0 and 1 as non-prime
    my_filter[0] = my_filter[1] = False

    # Precompute the cumulative count of primes up to each index
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y

    # Count the number of rounds Maria wins
    player1 = 0
    for x in nums:
        player1 += my_filter[x] % 2 == 1

    # Determine the winner based on the number of wins
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
