import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import odeint

try:
    print("TEST 1: SNAKE RANDOM WALK (Golden Source)...")
    x, y = [0], [0]
    for _ in range(50):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)
    plt.figure(figsize=(6,6))
    plt.plot(x, y, label='Snake Path', linewidth=2)
    plt.scatter(x[-1], y[-1], c='red', s=100, zorder=5, label='Head')
    plt.title('Snake Random Walk')
    plt.grid(True)
    plt.legend()
    plt.savefig('snake_final_test.png')
    print("SUCCESS: snake_final_test.png created.")
    plt.close()

    print("\nTEST 2: LORENZ ATTRACTOR (Golden Source)...")
    def lorenz(state, t, sigma=10, rho=28, beta=8/3):
        x, y, z = state
        return sigma * (y - x), x * (rho - z) - y, x * y - beta * z
    state0 = [1.0, 1.0, 1.0]
    t = np.arange(0.0, 40.0, 0.01)
    states = odeint(lorenz, state0, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(states[:, 0], states[:, 1], states[:, 2])
    ax.set_title('Lorenz Attractor')
    plt.savefig('lorenz_final_test.png')
    print("SUCCESS: lorenz_final_test.png created.")
    plt.close()
    
    print("\nTEST 3: ADVANCED HEATMAP (V42 Rules)...")
    data = np.random.rand(10, 10)
    plt.figure()
    plt.imshow(data, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title("Advanced Heatmap")
    plt.savefig('heatmap_test.png')
    print("SUCCESS: heatmap_test.png created.")
    plt.close()
    
    print("\nALL SYSTEMS PROVEN.")

except Exception as e:
    print(f"CRITICAL FAILURE: {e}")
    exit(1)
