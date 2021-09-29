import gym #ALL you have to do to import and use open ai gym
env = gym.make("FrozenLake-v1") #We are going to use the FrozenLake enviroment

print(env.observation_space.n) #get number of states
print(env.action_space.n) #get number of actions

env.reset()
action = env.action_space.sample()
observation, reward, done,info = env.step(action)
env.render() #Render the GUI for the enviroment