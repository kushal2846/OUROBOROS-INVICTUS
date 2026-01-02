# 🛡️ OUROBOROS: INVICTUS

**The Unconquered AI Coding Engine.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white_red.svg)](https://ouroboros-invictus-rt9dewshvgzvadam7qmxrm.streamlit.app/)

> *"It swallows its own tail to heal itself."*

Ouroboros Invictus is a self-correcting, multi-model AI coding environment designed to build, fix, and execute Python code in real-time. It features a military-grade fallback system that ensures functionality even when primary AI APIs fail.

## 🚀 Key Features

### 1. **Invictus Engine (Multi-Model Cascade)**
The system never gives up. It iterates through a prioritized list of AI models (`Gemini 1.5 Flash`, `1.5 Pro`, `1.0 Pro`, `Pro`) to find a working channel.

### 2. **Diamond Deep Scan (Discovery Mode)**
If all standard models fail (e.g., 404/429 errors), the engine performs a **Deep API Scan** (`list_models()`) to discover *any* model available to your API key, regardless of region or tier, and routes traffic through it.

### 3. **Infinity Reflexion (Recursive Repair)**
The engine catches its own runtime errors (like `NameError`, `TypeError`, or logic bugs). instead of crashing, it enters a **Reflexion Loop**:
-   It feeds the broken code + error message back to the AI.
-   It commands a fix.
-   It retries execution.
-   *Max Retries: 3.*

### 4. **Loudmouth Protocol**
Silent failures are treated as critical errors. If code runs but produces no output (text or images), Invictus forces a rewrite to ensure visibility.

### 5. **Universal Visualizer & auto-Healing**
-   **Omni-Link**: Automatically installs missing pip packages (`ModuleNotFoundError`).
-   **Visualizer**: Instantly displays any generated image (`*.png`, `*.jpg`).
-   **Headless-Safe**: Optimizes plots for serverless environments (no `plt.show()` crashes).

## 🛠️ Usage

### Installation
```bash
git clone https://github.com/kushal2846/OUROBOROS-INVICTUS.git
cd OUROBOROS-INVICTUS
pip install -r requirements.txt
```

### Running Locally
```bash
streamlit run ouroboros.py
```

### Modes
-   **Code Builder**: Describe a tool (e.g., "Make a Snake Game") and watch it build.
-   **Code Surgeon**: Paste broken code + error, and let Invictus perform surgery.

## 📦 Deployment

### Streamlit Cloud (Recommended)
1.  Push to GitHub.
2.  Connect repo to [share.streamlit.io](https://share.streamlit.io).
3.  Deploy.

### Vercel / Render / Railway
Configuration files (`Procfile`, `requirements.txt`) are included.
*Note: Streamlit requires a persistent server. For Vercel, ensure you are using a compatible runtime configuration or docker container.*

## 📜 License
MIT License. Copyright (c) 2026 Kushal.
