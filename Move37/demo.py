import gym

#env= gym.make('CartPole-v0')
env= gym.make('Hero-v4')

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
