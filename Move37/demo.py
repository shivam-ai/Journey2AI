import gym

<<<<<<< HEAD
env= gym.make('CartPole-v0')
env= gym.make('FrozenLake-v0')
=======
#env= gym.make('CartPole-v0')
env= gym.make('Hero-v4')
>>>>>>> e09bc97d17fbcd4138ea1216d9e1611b2262aad5

for i_episode in range(10):
    observation= env.reset()
    for k in range(100):
        env.render()
        print(observation)
        action= env.action_space.sample()
        observation, reward, done, info= env.step(action)
        if(done):
            print("Episode finished in {} timesteps.".format(k+1))
            #break
env.close()
