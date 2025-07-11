import math

def calculate_dominant_probability(k, m, n):
    # This is definitely more of a statistics problem, but we can simplify it with coding.

    # First we will need the total population.
    total_population = k + m + n 

    # Next, get all the possible combinations from the total population.
    all_combinations = math.comb(total_population, 2)

    # Next, we will find all the dominant alleles.
    # The math should be straight forward for non combinations: k * m being dom/het having 100%, k * n being dom/rec having 100%, 50% for het/rec.
    # The combinations are done for two of the same, since if we take one, we will have to take out another.
    # A creature cannot mate with itself in this example, which is why two doms and two hets are combinations.
    dominant_combinations = math.comb(k, 2) + k*m + k*n + .5*m*n + .75*math.comb(m, 2)

    dominant_probability = dominant_combinations/all_combinations
    return dominant_probability

with open("iprb/rosalind_iprb.txt", "r") as file:
    nums = file.readline().split(" ")
    print(calculate_dominant_probability(int(nums[0]), int(nums[1]), int(nums[2])))