# Import routines
import numpy as np
import math
import random
from itertools import product

# Defining hyperparameters
m = 5     # number of cities, ranges from 1 ..... m
t = 24    # number of hours, ranges from 0 .... t-1
d = 7     # number of days, ranges from 0 ... d-1
C = 5     # Per hour fuel and other costs
R = 9     # per hour revenue from a passenger

location_dist = [2, 12, 4, 7, 8]
full_action_space = [[0,0]] + [list(x) for x in list(product(np.arange(1,m+1), repeat=2)) if x[0] != x[1]]
full_state_space = [list(x) for x in list(product(np.arange(1,m+1), np.arange(1,t+1), np.arange(1,d+1)))]

class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = full_action_space.copy()
        self.state_space = full_state_space.copy()
        self.state_init = random.choice(self.state_space)

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input
    # def state_encod_arch1(self, state):
    #     """convert the state into a vector so that it can be fed to the NN. 
    #     This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""

    #     return state_encod

    def get_one_hot_encoded(self, size, location):
        """ Returns one hot encoded list """
        ohev = np.zeros(size)
        ohev[location] = 1
        return ohev


    # Use this function if you are using architecture-2 
    def state_encod_arch2(self, state, action):
        """Convert (state-action) into a vector so that it can be fed to the NN. 
        Convert a given state-action pair into a vector format. Hint: Vector is of size m + t + d + m + m."""

        state_encod = list(self.get_one_hot_encoded(m, state[0]-1)) + \
                        list(self.get_one_hot_encoded(t, state[1]-1)) + \
                        list(self.get_one_hot_encoded(d, state[2]-1))

        for x in [0,1]:
            if action[x] == 0:
                state_encod += list(np.zeros(m))
            else:
                state_encod += list(self.get_one_hot_encoded(m, action[x] - 1))
        
        return state_encod


    ## Getting number of requests
    def requests(self, state):
        """Determining number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0] - 1

        requests = np.random.poisson(location_dist[location])
        if requests > 15:
            requests = 15

        possible_actions_index = random.sample(range(1, (m-1)*m + 1), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_index]

        actions.append([0,0])

        return possible_actions_index, actions   


    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        reward = 0.0
        trip_time = 0

        if action == [0,0]:
            reward = (-1 * C)
            trip_time = 1
            return reward, trip_time

        curr_loc = state[0]
        curr_hour = state[1]
        curr_day = state[2]
        start_loc = action[0]
        end_loc = action[1]

        if curr_loc == start_loc:
            trip_time = int(Time_matrix[start_loc-1][end_loc-1][curr_hour-1][curr_day-1])
            reward += (trip_time * (R - C))
        else:
            # Negative Reward when moving from current location to start location
            time_from_curr_to_start_loc = int(Time_matrix[curr_loc-1][start_loc-1][curr_hour-1][curr_day-1])
            reward -= (time_from_curr_to_start_loc * C)
            trip_time += time_from_curr_to_start_loc

            # Positive Reward when moving from start location to end location
            drop_time = 0
            if (curr_hour + time_from_curr_to_start_loc) > 24:
                if curr_day == d:
                    curr_day = 1  # Sunday to Monday
                else:
                    curr_day += 1 # Crossed into next day

                drop_time = int(Time_matrix[start_loc-1][end_loc-1][curr_hour + time_from_curr_to_start_loc - 24 -1][curr_day-1])
            else:
                drop_time = int(Time_matrix[start_loc-1][end_loc-1][curr_hour + time_from_curr_to_start_loc - 1][curr_day-1])

            reward += (drop_time * (R - C))
            trip_time += drop_time
        
        return reward, trip_time


    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        next_state = state.copy()

        if action != [0,0]:
            curr_loc = state[0]
            curr_hour = state[1]
            curr_day = state[2]
            start_loc = action[0]
            end_loc = action[1]
            
            if curr_loc == start_loc:
                next_state[0] = end_loc
                next_state[2] = curr_day       
                
                next_hour = curr_hour + int(Time_matrix[start_loc-1][end_loc-1][curr_hour-1][curr_day-1])

                if next_hour > 24:
                    next_state[1] = (next_hour - 24)
                    if next_state[2] == d:
                        next_state[2] = 1
                    else:
                        next_state[2] += 1
                else:
                    next_state[1] = next_hour                    
            else:
                # Next state when moving from current location to start location
                next_state = self.next_state_func(next_state, [curr_loc, start_loc], Time_matrix)
                # Positive Reward when moving from start location to end location
                next_state = self.next_state_func(next_state, action, Time_matrix)

        return next_state


    def reset(self):
        return self.action_space, self.state_space, self.state_init