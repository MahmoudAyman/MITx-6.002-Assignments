"""
 * Copyright (c) 2019 Mahmoud Ayman
 * Email: mahmoud.ayman07@gmail.com
 * Website: www.betngana.com
 * Title: 6.002-PSet1.py
 *
 * This file is part of the MIT 6.002 course assignments, as taught in 2016 .
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *
 * YOU ARE FREE TO:
 *  - Share — copy and redistribute the material in any medium or format
 *  UNDER THE FOLLOWING TERMS:
 *      - Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were
 *      made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or
 *      your use.
 *  - NonCommercial — You may not use the material for commercial purposes.
 *  - NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified
 *  Material.
 * 
 * CREATED BY: MAHMOUD AYMAN (mahmoud.ayman07@gmail.com)
 * LICENSED BY THE AUTHOR UNDER (CC-BY-NC-ND-4.0)
 * https://creativecommons.org/licenses/by-nc-nd/4.0/
 """

from ps1_partition import get_partitions
import time
import operator
import random
import matplotlib.pyplot as plt
random.seed(0)
#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(fileName):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    data = {}
    lines = []
    with open(fileName) as f:
        lines = f.readlines()
    for i in lines:
        temp = i.split(",")
        # print (type(temp[1  ]))
        data[temp[0]] = int(temp[1])

    return data

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic  to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_sorted = sorted(cows.items(), key = operator.itemgetter(1), reverse = True)
    taken = [0]*(len(cows_sorted))
    counter = 0
    trips=[]
    while (counter < len(cows_sorted)):
        remaining_weight = limit
        currentTrip=[]
        for i in range(0,len(cows_sorted)):
            current_weight = cows_sorted[i][1]
            if (current_weight <= remaining_weight) and (taken[i] == False):
                currentTrip.append(cows_sorted[i][0])
                remaining_weight -= current_weight
                taken[i] = True
                counter +=1

            if (remaining_weight == 0):
                break
        trips.append(currentTrip)

    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    items = cows.keys()
    noCows = len(items)
    
    for i in get_partitions(items):
        # print("I:" +str(i))
        count = 0
        for j in i:
            # print("J:" +str(j))
            total_weight = 0
            for k in j:
                # print("K:" +str(k))
                total_weight+= cows[k]
                count+=1
                if total_weight > limit:
                    # print ("out of weight")
                    break

        if count == noCows:
            return i
        
# Problem 4

def generateRandCows(n):
    cows={}
    names = ['a', 'b', 'c','d', 'e','f','g', 'h', 'i','j', 'k','l','m', 'n', 'o','p', 'q','r','s', 't', 'v','u', 'w','x','y','z']
    selection = random.sample(names, n)
    for j in selection:
        val = random.randint(1,10)
        cows[j]=val
    return cows

def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    greedyTimes=[]
    bruteTimes=[]
    for i in range(1,16):
        print (i)
        cows = generateRandCows(i)
        start = time.time()
        greedy_cow_transport(cows)
        end = time.time()
        greedyTimes.append((end-start))
        start = time.time()
        brute_force_cow_transport(cows)
        end = time.time()
        bruteTimes.append((end-start))

    noCows = range(1,16)
    plt.plot(noCows, bruteTimes)
    plt.plot(noCows, greedyTimes)
    plt.legend(["Brute Force", "Greedy"], loc= 'upper left')

    plt.show()



# data = load_cows("ps1_cow_data_2.txt")
# #print (greedy_cow_transport(data))
# print (brute_force_cow_transport(data))

compare_cow_transport_algorithms()