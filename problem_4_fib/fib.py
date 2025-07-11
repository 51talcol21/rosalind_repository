# A classic in SWE/basic CS pattern solving: Dynamic Programming.
def dynamicRabbits(n: int, k: int):
    """
    Implement dynamic rabbits problem.

    Parameters:
        n: Month to stop at
        k: Value by which breed/offspring come from.

    Returns:
        Number of rabbits at the end.
    """
    # Instead of using recursion, we will implement dynamic programming.
    # Basically, we will do a bottom-up approach where we start with the lowest values and build our way up.
    # Like the Fibonacci Sequence, we can just use the two prior numbers to calculate the current.
    # We will store it in memory, also called memoization, rather than just calling a recursive
    # I.E., store in array, don't do Fib(n) = Fib(n-1) + Fib(n-2)

    # Initialize our array (basically month 0,1,2)
    bottomUpDP = [0,1,1]

    # For each month, we'll want to take the prior two values and add them (because it's recursive)
    # The only difference between this and the fibonacci sequence is the needed multiplication for rabbit breeding (k)
    for eachMonth in range(3,n+1):
        # For each month, we'll calculate and append it to end of array, go to next month, and use the prior value to do so.
        # And so on and so on.
        bottomUpDP.append(bottomUpDP[eachMonth - 1] + k * bottomUpDP[eachMonth - 2])

    # At this point, we've calculated every single value up to n.
    # This is better than recursion as instead of calculating the prior EVERY single recursion call, we just hold it in memory (bottomUpDP)
    # If you were to do recursion, imagine a branching tree to break down each value into two.
    # It will grow exponentially and return all the way up. This way, we only need to know the prior two and basically save our work.
    return bottomUpDP[-1]

if __name__ == "__main__":
    with open("problem_4_fib/rosalind_fib.txt", "r") as file:
        nums = file.readline().split(" ")
        n = int(nums[0])
        k = int(nums[1])
    print(dynamicRabbits(n, k))
