'''Modification of the code available in python notebook by simoninithomas
https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Q%20learning/Q%20Learning%20with%20FrozenLake.ipynb
'''


import numpy as np
import gym
import random



env = gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=False)
action_size = env.action_space.n
state_size = env.observation_space.n

qtable = np.zeros((state_size, action_size))
#print(qtable)

total_episodes = 50        # Total episodes
learning_rate = 0.8         # Learning rate
max_steps = 20              # Max steps per episode
gamma = 0.5                 # Discounting rate

# Exploration parameters
epsilon = 1.0                 # Exploration rate
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.01            # Minimum exploration probability 
decay_rate = 0.01            # Exponential decay rate for exploration prob

# List of rewards
rewards = []

# 2 For life or until learning is stopped
for episode in range(total_episodes):
    # Reset the environment
    state = env.reset()
    step = 0
    done = False
    total_rewards = 0
    print("EPISODE",episode)
    
    for step in range(max_steps):
        # 3. Choose an action a in the current world state (s)
        ## First we randomize a number
        exp_exp_tradeoff = random.uniform(0, 1)
        
        ## If this number > greater than epsilon --> exploitation (taking the biggest Q value for this state)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state,:])
            #print("Let's exploit.", action)
            env.render()

        # Else doing a random choice --> exploration
        else:
            action = env.action_space.sample()
            #print("Let's explore.",action)
            env.render()

        # Take the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done, info = env.step(action)
        
        #Somehow, the environment does not give negative rewards for game over, so hack it:
        if done and reward == 0:
            reward = -5
        if new_state == state:
            reward = -1
        print("NEW STATE:",new_state,"REWARD:",reward)

        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        # qtable[new_state,:] : all the actions we can take from new state
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])
        print("QTABLE AT",state,qtable[state])
        
        total_rewards += reward
        
        # Our new state is state
        state = new_state
        
        # If done (if we're dead) : finish episode
        if done: 
            print("GAME OVER.\n\n")
            break
        
    episode += 1
    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
    print(epsilon)
    rewards.append(total_rewards)

print ("Score over time: " +  str(sum(rewards)/total_episodes))
print(qtable)




env.reset()

for episode in range(0):
    state = env.reset()
    step = 0
    done = False
    print("****************************************************")
    print("EPISODE ", episode)

    for step in range(max_steps):
        env.render()
        # Take the action (index) that have the maximum expected future reward given that state
        action = np.argmax(qtable[state,:])
        
        new_state, reward, done, info = env.step(action)
        
        if done:
            break
        state = new_state
env.close()


