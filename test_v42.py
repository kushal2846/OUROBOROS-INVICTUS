import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import networkx as nx
from skimage import data, filters
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

try:
    print("TEST 1: SCIKIT-IMAGE (Advanced Vision)...")
    image = data.camera()
    edges = filters.sobel(image)
    plt.imshow(edges, cmap='gray')
    plt.savefig('test_vision.png')
    print("Visual Success.")

    print("\nTEST 2: SCIKIT-LEARN (ML)...")
    X = np.array([[1], [2], [3], [4]])
    y = np.dot(X, np.array([2])) + 3
    reg = LinearRegression().fit(X, y)
    print(f"ML Prediction: {reg.predict(np.array([[5]]))}")

    print("\nTEST 3: NETWORKX (Graph Theory)...")
    G = nx.complete_graph(5)
    nx.draw(G)
    plt.savefig('test_graph.png')
    print("Graph Success.")

    print("\nTEST 4: STATSMODELS (Advanced Stats)...")
    dta = sm.datasets.macrodata.load_pandas().data
    print(f"Stats Data Loaded: {dta.shape}")

    print("\nALL SYSTEMS (ARSENAL) PROVEN.")

except Exception as e:
    print(f"CRITICAL FAILURE: {e}")
    exit(1)
