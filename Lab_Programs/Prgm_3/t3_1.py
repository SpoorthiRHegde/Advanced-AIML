import random

# Sample space: rolling a fair six-sided die
sample_space = [1, 2, 3, 4, 5, 6]

# Event: rolling an even number
event = {2, 4, 6}

# Probability of event = favorable outcomes / total outcomes
prob_event = len(event) / len(sample_space)
print(f"Sample space: {sample_space}")
print(f"Event (Even numbers): {event}")
print(f"Probability of event = {prob_event:.2f}")

# Simulate experiment: roll die 10 times
trials = 10
outcomes = [random.choice(sample_space) for _ in range(trials)]
print(f"Simulated outcomes: {outcomes}")
