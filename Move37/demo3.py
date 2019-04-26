import gym
import numpy as np


env= gym.make('CartPole-v0')

parameters = np.random.rand(4) * 2 - 1 
print(parameters)

'''
observation= env.reset()

for k in range(200):
    env.render()
    print(observation)
    #action= env.action_space.sample()
    action= 0 if np.matmul(parameters, observation) < 0 else 1 
    observation, reward, done, info= env.step(action)
'''

def run_episode(env, parameters):
    observation= env.reset()
    totalreward= 0
    for _ in range(200):
        action= 0 if np.matmul(parameters, observation) < 0 else 1
        env.render()
        observation, reward, done, info= env.step(action)
        totalreward+= reward
        if(done):
            break
    return totalreward





bestparams= None
bestreward= 0

# Random serarch
for i in range(100):
    parameters= np.random.rand(4) * 2-1 
    reward= run_episode(env, parameters)
    print("reward in {} episode is {}".format(i, reward))
    if(reward > bestreward):
        bestreward= reward
        bestparams= parameters
        print("Best reward in {} episoeds is {}".format(i, bestreward))
        if(reward == 200):
            print("Done")
            break
'''


# Hill Climbing
noise_scaling= 0.01
parameters= np.random.rand(4) * 2-1 
for i in range(100):
    newparams= parameters + (np.random.rand(4) * 2 - 1) * noise_scaling
    reward= run_episode(env, newparams)
    if(reward > bestreward):
        bestreward= reward
        parameters= newparams
        print("Best reward in {} episoeds is {}".format(i, bestreward))
        if(reward == 200):
            print("Done")
            break
'''

env.close()
