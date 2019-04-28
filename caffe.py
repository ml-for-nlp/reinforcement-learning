import numpy as np
import random

environment = {
	0: [('buongiorno',[[1,0,1]]),('un caffè',[[7,0,1]])],
	1: [('un caffè',[[2,0,0.8],[12,-2,0.2]])],
	2: [('per favore',[[3,0,1]]),('EOS',[[5,-2,0.9],[6,-1,0.1]])],
	3: [('EOS',[[4,-1,1]])],
	7: [('per favore',[[8,0,1]]),('EOS',[[9,-3,1]])],
	8: [('EOS',[[10,-2,0.9],[11,-1,0.1]])]
	}

#index to actions
i_to_actions = {0: 'buongiorno', 1: 'un caffè', 2: 'per favore', 3: 'EOS'}
actions_to_i = {'buongiorno':0, 'un caffè':1, 'per favore':2, 'EOS':3}

#Initialising the Q matrix
q_matrix = []
for i in range(13):
    q_matrix.append([0,0,0,0])

exit_states = [4,5,6,9,10,11,12]

def get_possible_next_actions(cur_pos):
    return environment[cur_pos]

def get_next_state(action):
    word = action[0]
    possible_states = action[1]
    fate = {}
    for p in possible_states:
        s = p[0]
        r = p[1]
        l = p[2]
        fate[s] = [r,l]
    next_state = np.random.choice(list(fate.keys()),1,[v[1] for k,v in fate.items()])
    reward = fate[next_state[0]][0]
    #print(next_state[0],reward)
    return next_state[0],reward

def game_over(cur_pos):
    return cur_pos in exit_states

discount = 0.9
learning_rate = 0.1

for _ in range(500):
    print("\nEpisode ", _ )
    # get starting place
    cur_pos = 0
    # while goal state is not reached
    episode_return = 0
    while(not game_over(cur_pos)):
        # get all possible next states from cur_step
        possible_actions = get_possible_next_actions(cur_pos)
        # select any one action randomly
        action = random.choice(possible_actions)
        word = action[0]
        action_i = actions_to_i[word]
        print(word)
        # find the next state corresponding to the action selected
        next_state,reward = get_next_state(action)
        episode_return+=reward
        # update the q_matrix
        q_matrix[cur_pos][action_i] = q_matrix[cur_pos][action_i] + learning_rate * (reward + discount * max(q_matrix[next_state]) - q_matrix[cur_pos][action_i])
        print(cur_pos,q_matrix[cur_pos],next_state)
        # go to next state
        cur_pos = next_state
    print("Reward:",episode_return,"\n")

print(np.array(q_matrix).reshape(13,4))
print("Training done...")

print("\n***\nTesting...\n***\n")
# get starting place
cur_pos = 0
episode_return = 0
while(not game_over(cur_pos)):
    # get all possible next states from cur_step
    possible_actions = get_possible_next_actions(cur_pos)
    #print(possible_actions)
    # select the *possible* action with highest Q value
    action = None
    if np.linalg.norm(q_matrix[cur_pos]) == 0:
        action = random.choice(possible_actions)
    else:
        action = actions_to_i[possible_actions[0][0]]
        c = 0
        action_i = c
        for a in possible_actions:
            a_i = actions_to_i[a[0]]
            if q_matrix[cur_pos][a_i] > q_matrix[cur_pos][action]:
                action = a_i
                action_i = c
            c+=1
        action = possible_actions[action_i]
    print(action[0])
    next_state,reward = get_next_state(action)
    episode_return+=reward
    cur_pos = next_state
print("Return:",episode_return)
