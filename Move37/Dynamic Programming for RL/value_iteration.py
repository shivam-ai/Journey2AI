import numpy as np
from grid_world import standard_grid
from utils import print_policy, print_values
from grid_world import Grid


SMALL_ENOUGH= 1e-3
GAMMA= 0.9

ALL_POSSIBLE_ACTIONS= ('U', 'D', 'L', 'R')

def best_action_value(grid, V, s):
    best_a= None
    best_value= float('-inf')
    grid.set_state(s)

    for a in ALL_POSSIBLE_ACTIONS:
        transitions= grid.get_transition_probs(a)
        expected_r= 0
        expected_v= 0
        for (prob, r, s_prime) in transitions:
            expected_r= prob * r
            expected_v= prob * V[s_prime]
        v= expected_r + GAMMA * expected_v
        if(v > best_value):
            best_value= v
            best_a= a
    return best_a, best_value 


def calculate_values(grid):
    V= {}
    states= grid.all_states()
    for s in states:
        V[s]= 0
    print("Before")
    print(V)
    while(True):
        biggest_change= 0
        for s in grid.non_terminal_states():
            old_v= V[s]
            _, new_v= best_action_value(grid, V, s)
            V[s]= new_v
            biggest_change= max(biggest_change, abs(old_v- new_v))

        if(biggest_change< SMALL_ENOUGH):
            break
        print('Next values are :') 
        print_values(V, grid)
        print('.'*30)
    return V 

def initialize_random_policy(grid):
    policy= {}
    for s in grid.non_terminal_states():
        policy[s]= np.random.choice(ALL_POSSIBLE_ACTIONS)
    return policy

def calculate_greedy_policy(grid, V):
    policy= initialize_random_policy(grid)
    for s in policy.keys():
        grid.set_state(s)
        best_a, _ = best_action_value(grid, V, s)
        policy[s]= best_a
    return policy


if(__name__== '__main__'):
    grid= standard_grid(obey_prob=1.0, step_cost=None)
    print("Rewards: ")
    print_values(grid.rewards, grid)

    V= calculate_values(grid)

    policy= calculate_greedy_policy(grid, V)

    print("Values: ")
    print_values(V, grid)
    print("Policies: ")
    print_policy(policy, grid)