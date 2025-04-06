with open('dna.txt', 'r') as file:
    lines = file.readlines()

s = lines[0].strip()
t = lines[1].strip()

distance = 0

for a, b in zip(s, t):
    if a !=b:
        distance += 1

print("Humming Distance:", distance)
