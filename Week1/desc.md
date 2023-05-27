Referring to bandit.py -

Line 1-2 => Importing the required libraries 

Line 5-19 => I have created the 5 buttons with the different probability distribution given to us using numpy 

Now onwards is the implementation of the epsilon-greedy problem. 

Initializing Q and N where Q is the estimated reward and N is the number of times the action was performed or the button was pressed(This is used to update the action-value estimates.

Reward is an array to store all the rewards for 1000 episodes.

In one episode there is 100 time-steps so I have created a for loop for it. The if else statement choose whether to exploit or explore depending on the epsilon.

Now the action selected will update the N array and according to the action, it will press one of the buttons. 
After that, we are updating the estimated value of action reward (or action-value).
Summing the rewards of 100 timesteps using the 'episode_reward += reward'
Rewards is appended to the array for every episode.
Till this it was the defination of the function. Now we will use it.
We had to consider 3 epsilons and according to that I called the epsilon_greedy function thrice and the reward_curves now has all the episodes reward according to the epsilon.

Now for plotting I used matplotlib. And plotted the rewards vs episode for all three epsilons. 


PS- For the base code, I have used chatGPT.
