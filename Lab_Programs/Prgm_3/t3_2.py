import random

sample_space = ["rain", "sun", "cloudy"]
event = {"rain"}   # event of interest
prob = len(event) / len(sample_space)
print("Sample space:", sample_space)
print("Event:", event)
print("P(Event) =", prob)

# simulate 5 days of weather
print("Outcomes:", [random.choice(sample_space) for _ in range(5)])
