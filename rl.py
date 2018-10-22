import gym
import numpy as np
env = gym.make('CartPole-v0')
# for i_episode in range(20):
#     observation = env.reset()
#     for t in range(100):
#         env.render()
#         print(observation)
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
## Defining Parameters, action and episode
parameters = np.random.rand(4) * 2 - 1 
ep_vals = []
def run_episode(env, parameters):  
    observation = env.reset()
    totalreward = 0
    for t in range(200):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            ep_vals.append(t+1)
            break
    return totalreward

## Random Search
#  Generates random parameters each time till we get a successful one
# bestparams = None  
# bestreward = 0  
# for _ in range(10000):  
#     parameters = np.random.rand(4) * 2 - 1
#     reward = run_episode(env,parameters)
#     if reward > bestreward:
#         bestreward = reward
#         bestparams = parameters
#         # considered solved if the agent lasts 200 timesteps
#         if reward == 200:
#             break
# print('Number of episodes taken this run: '+ str(len(ep_vals)))

## Hill Climbing
#  Classic Gradient Descent
bestparams = None  
bestreward = 0  
for _ in range(10000):  
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env,parameters)
    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        # considered solved if the agent lasts 200 timesteps
        if reward == 200:
            break
print('Number of episodes taken this run: '+ str(len(ep_vals)))