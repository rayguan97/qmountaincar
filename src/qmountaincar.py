""" Q-Learning implementation for Cartpole """

import gym
import numpy as np
import collections
import math

env = gym.make('MountainCar-v0')
np.set_printoptions(threshold=np.inf)
# hyperparameters
buckets=(15, 15,) #this is a continuous case, we need to give them a range
n_episodes=10000
goal_reward=-195
min_alpha=0.3  # learning rate
min_epsilon=0.0  # exploration rate
gamma=1.0  # discount factor
ada_divisor=25
Q = np.zeros(buckets + (env.action_space.n,))



# helper functions
def discretize(obs):
    upper_bounds = [env.observation_space.high[0], env.observation_space.high[1]]
    lower_bounds = [env.observation_space.low[0], env.observation_space.low[1]]
    ratios = [(obs[i] + abs(lower_bounds[i])) / (upper_bounds[i] - lower_bounds[i]) for i in range(len(obs))]
    new_obs = [int(round((buckets[i] - 1) * ratios[i])) for i in range(len(obs))]
    new_obs = [min(buckets[i] - 1, max(0, new_obs[i])) for i in range(len(obs))]
    return tuple(new_obs)



def choose_action(state, epsilon):
    return env.action_space.sample() if (np.random.random() <= epsilon) else np.argmax(Q[state])

def update_q(state_old, action, reward, state_new, alpha):
    Q[state_old][action] += alpha * (reward + gamma * np.max(Q[state_new]) - Q[state_old][action])

def get_epsilon(t):
    return max(min_epsilon, min(1, 1.0 - math.log10((t + 1) / ada_divisor)))

def get_alpha(t):
    return max(min_alpha, min(1.0, 1.0 - math.log10((t + 1) / ada_divisor)))


def run_episode():
    """Run a single Q-Learning episode"""
    # get current state
    observation = env.reset()
    current_state = discretize(observation)

    # get learning rate and exploration rate
    alpha = get_alpha(episode)
    epsilon = get_epsilon(episode)

    done = False
    total_reward = 0

    # one episode of q learning
    while not done:
        # env.render()
        action = choose_action(current_state, epsilon)
        obs, reward, done, _ = env.step(action)
        new_state = discretize(obs)
        update_q(current_state, action, reward, new_state, alpha)
        current_state = new_state
        total_reward = total_reward + reward
    
    return total_reward


def visualize_policy():
    """Visualize current Q-Learning policy without exploration / learning"""
    current_state = discretize(env.reset())
    done=False

    while not done:
        action = choose_action(current_state, 0)
        obs, reward, done, _ = env.step(action)
        env.render()
        current_state = discretize(obs)

    # env.close()

    return


if __name__ == '__main__':
    rewards = collections.deque(maxlen=100)

    for episode in range(n_episodes):
        reward = run_episode()
        
        # mean reward of last 100 episodes
        rewards.append(reward)
        mean_reward = np.mean(rewards)

        # check if our policy is good
        if mean_reward >= goal_reward and episode >= 5000:
            print('Ran {} episodes. Solved after {} trials'.format(episode, episode - 100))
            print(mean_reward)
            visualize_policy()
            visualize_policy()
            visualize_policy()
            visualize_policy()
            print(Q)
            break
        
        elif episode % 100 == 0:
            print('[Episode {}] - Mean time over last 100 episodes was {} frames.'.format(episode, mean_reward))
