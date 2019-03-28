import numpy as np

class Grid:

    def __init__(self, width, height, start):
        # i is horizontal axis
        # j is vertical axis
        self.width= width
        self.height= height
        self.i= start[0]
        self.j= start[1]

    def set(self, rewards, actions, obey_prob):
        # rewards is dict of (i, j): r(row, col): reward
        # actions is dict of (i, j): A(row, col): list of possible actions
        self.rewards= rewards
        self.actions= actions
        self.obey_prob= obey_prob

    def non_terminal_states(self):
        return self.actions.keys()

    def set_state(self, s):
        self.i, self.j= s

    def current_state(self):
        return (self.i, self.j)

    def is_terminal(self, s):
        return s not in self.actions

    def check_move(self, action):
        i, j= self.i, self.j
        if(action in self.actions[(i, j)]):
            if(action== 'U'):
                j+= 1
            elif(action== 'D'):
                j-= 1
            elif(action== 'L'):
                i-= 1
            elif(action== 'R'):
                i+= 1
        reward= self.rewards.get((i, j), 0)
        return ((i, j), reward)
    
    def get_transition_probs(self, action):
        probs= []
        state, reward= self.check_move(action)
        probs.append((self.obey_prob, reward, state))
        disobey_prob= 1- self.obey_prob
        if(disobey_prob<= 0):
            return probs
        if(action== 'U' or action== 'D'):
            state, reward= self.check_move('L')
            probs.append((disobey_prob/2, reward, state))
            state, reward= self.check_move('R')
            probs.append((disobey_prob/2, reward, state))
        elif(action== 'L' or action== 'R'):
            state, reward= self.check_move('U')
            probs.append((disobey_prob/2, reward, state))
            state, reward= self.check_move('D')
            probs.append((disobey_prob/2, reward, state))
        return probs

    def game_over(self):
        return (self.i, self.j) not in self.actions

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())




def standard_grid(obey_prob= 1.0, step_cost= None):
    # .  .  .  1
    # .  x  . -1
    # s  .  .  .
    g= Grid(4, 3, (0,0))
    rewards= {(3, 2):1, (3, 1):-1}
    actions= {
        (0, 0): ('U', 'R'),
        (0, 1): ('U', 'D'),
        (0, 2): ('D', 'R'),
        (1, 0): ('L', 'R'),
        (1, 2): ('L', 'R'),
        (2, 0): ('L', 'R', 'U'),
        (2, 1): ('U', 'D'),
        (2, 2): ('L', 'R', 'D'),
        (3, 0): ('U', 'L')
    }
    g.set(rewards, actions, obey_prob)
    return g


    
