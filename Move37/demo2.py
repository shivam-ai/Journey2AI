import gym

env= gym.make('CartPole-v0')

env.reset()

print(env.action_space)
print("-"*40)
print(env.observation_space)


from gym import spaces
space= spaces.Discrete(5)
print(space)
x= space.sample()
assert space.contains(x)
assert space.n== 5


from gym import envs
print(len(envs.registry.env_specs))
for e in envs.registry.env_specs:
    print(e) 

    