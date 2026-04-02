import random

data_points = []

for _ in range(100):
    k1 = (random.gauss(6), random.gauss(6))
    k2 = (random.gauss(2), random.gauss(6))
    k3 = (random.gauss(6), random.gauss(2))
    k4 = (random.gauss(2), random.gauss(2))
    data_points.extend([k1,k2,k3,k4])


with open("fake_clusters_4_v2.csv", "w") as f:
    f.write("x,y\n")
    for p in data_points:
        f.write(f"{p[0]},{p[1]}\n")