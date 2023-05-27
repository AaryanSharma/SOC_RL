import numpy as np
import matplotlib.pyplot as plt

# Define the reward functions for each button
def button_1():
    return np.random.normal(2, 1)

def button_2():
    return np.random.choice([-6, 5])

def button_3():
    return np.random.poisson(2)

def button_4():
    return np.random.exponential(3)

def button_5():
    button = np.random.choice([button_1, button_2, button_3, button_4])
    return button()

def epsilon_greedy(epsilon):
    # Initialize action-value estimates and action counts
    Q = np.zeros(5)
    N = np.zeros(5)
    rewards = []

    # Run episodes
    for episode in range(1000):
        episode_reward = 0

        # Choose an action for each time step
        for step in range(100):
            # Choose an action
            if np.random.random() < epsilon:
                action = np.random.randint(5)  # Explore
            else:
                action = np.argmax(Q)  # Exploit

            # Update action counts
            N[action] += 1

            # Get reward
            if action == 0:
                reward = button_1()
            elif action == 1:
                reward = button_2()
            elif action == 2:
                reward = button_3()
            elif action == 3:
                reward = button_4()
            else:
                reward = button_5()

            # Update action-value estimates
            Q[action] += (1 / N[action]) * (reward - Q[action])

            episode_reward += reward

        rewards.append(episode_reward)

    return rewards

# Set the epsilon values to test
epsilons = [0.1, 0.01, 0]

# Run epsilon-greedy for each epsilon value
reward_curves = []
for epsilon in epsilons:
    rewards = epsilon_greedy(epsilon)
    reward_curves.append(rewards)

# Plot the reward curves
# plt.figure(figsize=(10, 6))
for epsilon, rewards in zip(epsilons, reward_curves):
    plt.plot(range(len(rewards)), rewards, label=f"Epsilon = {epsilon}")
plt.yticks(np.arange(0, 550, 50))
plt.xlabel("Episode")
plt.ylabel("Reward at the end of episode")
plt.legend()
plt.show()
