import matplotlib.pyplot as plt

def collatz(num, steps_taken, highest_value):
    if num == 1:
        return steps_taken

    if num > highest_value:
        highest_value = num
    
    if num % 2 == 0:
        return collatz(num / 2, steps_taken + 1, highest_value)
    else:
        return collatz(3 * num + 1, steps_taken + 1, highest_value)

iterations = 10000

collatz_values = []
colors = []

for each in range(1,iterations):
    collatz_values.append(collatz(each, 0, each))

    if each % 2 == 0:
        colors.append('tab:orange')
    elif each % 3 == 0:
        colors.append('tab:purple')
    else:
        colors.append('tab:blue')

plt.scatter(range(1, iterations), collatz_values, c=colors, s=10)

plt.xlabel('Value')
plt.ylabel('Steps taken to reach 1')
plt.title(f"Collatz Conjecture: Number of steps for values 1-{iterations}")

plt.show()