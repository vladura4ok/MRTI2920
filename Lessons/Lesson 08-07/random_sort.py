import random

def is_sorted(coll):

    current_order = coll[1] >= coll[0]

    for i in range(2, len(coll)):
        if (coll[i] >= coll[i-1]) != current_order:
            return False

    return True

def get_random_index(low_bound, high_bound):
    return random.randint(low_bound, high_bound)

def random_swap(coll):
    left_index = get_random_index(0, len(coll)-1)
    right_index = get_random_index(0, len(coll)-1)

    while left_index == right_index:
        right_index = get_random_index(0, len(coll)-1)

    coll[left_index], coll[right_index] = coll[right_index], coll[left_index]
        

def random_sort(coll):

    attempt_counter = 0
    while not is_sorted(coll):
        attempt_counter += 1
        print(f"attempt number {attempt_counter}")
        random_swap(coll)

    print("sorted!")

x = [7,1,4,5,3,2,6]

random_sort(x)
    