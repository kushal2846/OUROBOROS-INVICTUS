import subprocess, sys

# --- A. PLATINUM SETUP & AUTO-FIX ---
required_libs = {'streamlit': 'streamlit', 
                 'streamlit_antd_components': 'streamlit-antd-components',
                 'google.generativeai': 'google-generativeai',
                 'matplotlib': 'matplotlib'}

for lib_name, pip_name in required_libs.items():
    try:
        __import__(lib_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

import streamlit as st
import streamlit_antd_components as sac
import google.generativeai as genai
import subprocess
import sys
import os
import time
import re
import glob
from typing import Dict

# CRITICAL PATH FIX: Always execute in current CWD
current_dir = os.getcwd()
exec_path = os.path.join(current_dir, "ouroboros_exe_v21.py")

# --- B. PLATINUM CSS (OBSIDIAN & ROYAL BLUE) ---
st.set_page_config(
    page_title="OUROBOROS: INVICTUS",
    page_icon="�️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Colors: Obsidian #0a0a0a, Royal Blue #3b82f6, Gold #fbbf24, Green #10b981
PLATINUM_CSS = """
<style>
/* 1. PROFESSIONAL ANIMATIONS */
@keyframes slide-up {
    0% { transform: translateY(10px); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
}

/* 2. THEME BASE */
.stApp { background-color: #050505; color: #f3f4f6; font-family: 'Inter', system-ui, sans-serif; }

/* 3. INPUT DECK (Clean Professional) */
.stTextArea > div > div > textarea {
    background-color: #111 !important;
    border: 1px solid #333 !important;
    color: #e5e7eb !important;
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    border-radius: 6px;
}
.stTextArea > div > div > textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
}

/* 4. TERMINAL (High Contrast) */
.terminal-card {
    background-color: #000;
    border: 1px solid #1f2937;
    border-left: 4px solid #3b82f6; /* Royal Blue Accent */
    border-radius: 6px;
    padding: 16px;
    font-family: 'Consolas', monospace;
    color: #cbd5e1;
    font-size: 0.9em;
    line-height: 1.5;
    white-space: pre-wrap;
    animation: slide-up 0.4s ease-out;
}
.error-card {
    border-left-color: #ef4444; 
    color: #fca5a5;
    background-color: rgba(239, 68, 68, 0.05);
}

/* 5. HUD CARD */
.hud-card {
    background: linear-gradient(145deg, #0f172a, #0a0a0a);
    border: 1px solid #1e293b;
    border-radius: 8px;
    padding: 12px 20px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
}
.hud-progress-track {
    width: 60%;
    height: 6px;
    background: #1e293b;
    border-radius: 3px;
    overflow: hidden;
}
.hud-progress-bar {
    height: 100%;
    background: #3b82f6;
    border-radius: 3px;
    transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

/* 6. BUTTONS */
button[kind="primary"] {
    background-color: #3b82f6 !important;
    color: white !important;
    border: none;
    font-weight: 600;
    border-radius: 6px;
    transition: all 0.2s;
}
button[kind="primary"]:hover {
    background-color: #2563eb !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

h1, h2, h3 { color: #f3f4f6 !important; letter-spacing: -0.5px; }
div[data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #222; }
</style>
"""
st.markdown(PLATINUM_CSS, unsafe_allow_html=True)

# --- C. SYSTEM CORE ---

def clean_artifacts():
    """Universal Cleanup: Nuke ALL images and execution scripts"""
    patterns = ["*.png", "*.jpg", "*.jpeg", "*.svg", "ouroboros_exe_*.py"]
    for p in patterns:
        for f in glob.glob(p):
            try: os.remove(f)
            except: pass

class InvictusEngine:
    def __init__(self, key):
        genai.configure(api_key=key)
        self.key = key
        # INVICTUS MODEL CASCADE (Updated with fallback to discovery)
        self.models = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-1.0-pro', 'gemini-pro']

    def discover_models(self):
        """Emergency Discovery Mode"""
        try:
            found = []
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    found.append(m.name)
            return found
        except Exception as e:
            return []

    def generate(self, prompt, mode="architect", error_context=None, status_ph=None):
        base_instruct = (
            "You are a professional Python engineer. Return ONLY raw executable code. No markdown fences.\n"
            "IMPORTS:\n"
            "- If using matplotlib, you MUST write exactly this sequence:\n"
            "  import matplotlib\n"
            "  matplotlib.use('Agg')\n"
            "  import matplotlib.pyplot as plt\n"
            "- CRITICAL RULE: For 3D plots, use `ax.scatter(c=array)`. Do NOT use `ax.plot(c=array)`.\n"
            "- VISUALS: If creating an image, save it as a PNG file (e.g., 'chart.png'). DO NOT use `plt.show()`.\n"
            "- NUMPY RULE: Verify array shapes. Do NOT use `len()` on scalar numpy types (float64).\n"
            "- DECORATOR RULE: Wrappers MUST accept `*args` and `**kwargs` to avoid TypeError.\n"
            "- OUTPUT RULE: Silent success is failure. PROVE your work by printing the final result or saving a plot.\n"
            "- ALIAS RULE: Do NOT import 'plt'. Use `import matplotlib.pyplot as plt`. Do NOT import 'cv2' without installing `opencv-python`.\n"
            "- IMPORT RULE: Do NOT import 'shift', 'utils', or other imaginary modules. Only use Standard Library or PyPI packages.\n"
            "- LOGIC RULE: Ensure coordinate tuples (x,y) are consistent. Do not mix 2D and 3D coordinates.\n"
            "- If asking for a game, write a non-interactive simulation (500 steps) and print results.\n"
            "- PRINT ALL OUTPUTS TO STDOUT."
        )
        
        if mode == "surgeon":
            full_prompt = (
                f"{base_instruct}\n\n"
                f"DEBUG TASK: Fix this broken code based on the error.\n"
                f"ERROR:\n{error_context}\n\n"
                f"BROKEN CODE:\n{prompt}"
            )
        else:
            full_prompt = f"{base_instruct}\n\nTASK: {prompt}"

        # 1. TITANIUM LOOP: Try every model in the cascade
        last_error = ""

        # V30 OMEGA: Force Headless Config in Prompt
        if "matplotlib" in full_prompt.lower() or "plot" in full_prompt.lower():
             full_prompt = "You MUST start your code with:\nimport matplotlib\nmatplotlib.use('Agg')\n\n" + full_prompt

        for model_name in self.models:
            try:
                # Update HUD if we are retrying
                if status_ph and model_name != self.models[0]:
                    status_ph.markdown(render_hud(f"REROUTING: {model_name.upper()}...", 50, "#eab308"), unsafe_allow_html=True)
                
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(full_prompt)
                return re.sub(r'^```[a-zA-Z]*\n|\n```$', '', response.text.strip())
            
            except Exception as e:
                last_error = str(e)
                # Cool down to prevent 429s (Reduced for Speed V34)
                time.sleep(0.5) 
                continue
        
        # 2. DIAMOND DISCOVERY (Emergency)
        if status_ph:
            status_ph.markdown(render_hud("DIAGNOSTIC SCAN INITIATED...", 75, "#a855f7"), unsafe_allow_html=True)
        
        found_models = self.discover_models()
        
        if found_models:
            # V22 UPGRADE: Deep Scan - Try ALL found models
            for i, valid_model in enumerate(found_models):
                try:
                    if status_ph:
                        status_ph.markdown(render_hud(f"DIAGNOSTIC TRY ({i+1}/{len(found_models)}): {valid_model}", 80, "#a855f7"), unsafe_allow_html=True)
                    
                    model = genai.GenerativeModel(valid_model)
                    response = model.generate_content(full_prompt)
                    return re.sub(r'^```[a-zA-Z]*\n|\n```$', '', response.text.strip())
                except Exception as e:
                    last_error = f"Model {valid_model} failed: {e}"
                    time.sleep(1) # Slight cool down
                    continue
        else:
            last_error += " | Diagnostic Scan: No models found."

        # Final Failure
        error_msg = f"Diamond System Failure: All routes exhausted. Last error: {last_error}"
        return f"print({repr(error_msg)})"

    def execute_with_healing(self, code, status_ph):
        """Self-Healing Execution Loop"""
        clean_artifacts()
        
        with open(exec_path, "w", encoding='utf-8') as f: f.write(code)
        
        max_retries = 3
        attempt = 1
        
        while attempt <= max_retries:
            try:
                # EXECUTE
                res = subprocess.run(
                    [sys.executable, exec_path],
                    capture_output=True, text=True, timeout=45, cwd=current_dir
                )
                
                # CHECK FOR MISSING MODULES (PIP & SMART ALIASES)
                if res.returncode != 0 and "ModuleNotFoundError" in res.stderr:
                    match = re.search(r"No module named '(\w+)'", res.stderr)
                    if match:
                        missing_lib = match.group(1)
                        status_ph.markdown(render_hud(f"HEALING: DIAGNOSING {missing_lib.upper()}...", 60 + (attempt*10), "#ef4444"), unsafe_allow_html=True)
                        
                        # V31 SMART HEALER: Logic for Aliases
                        if missing_lib == "plt":
                            # Fix Code directly
                            status_ph.markdown(render_hud(f"HEALING: REPLACING 'import plt' -> 'import matplotlib.pyplot as plt'...", 70, "#10b981"), unsafe_allow_html=True)
                            code = code.replace("import plt", "import matplotlib.pyplot as plt")
                            with open(exec_path, "w", encoding='utf-8') as f: f.write(code)
                            attempt += 1
                            continue
                        
                        # Map common import names to Pip package names
                        pip_map = {
                            "sklearn": "scikit-learn",
                            "cv2": "opencv-python-headless",
                            "PIL": "Pillow",
                            "skimage": "scikit-image"
                        }
                        install_name = pip_map.get(missing_lib, missing_lib)
                        
                        try:
                            # Use --user to avoid permission errors on Cloud
                            subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", install_name])
                            attempt += 1
                            continue # RETRY LOOP
                        except Exception as e:
                            # V29: HALLUCINATION FIREWALL -> Refined
                            error_msg = (
                                f"CRITICAL ERROR: The module '{missing_lib}' (Pip: {install_name}) FAILED to install.\n"
                                f"It likely does not exist or is incompatible.\n"
                                f"ACTION: Rewrite code to NOT use '{missing_lib}'."
                            )
                            return {"success": False, "stdout": "", "stderr": error_msg, "code": code}

                # CHECK FOR MISSING IMPORTS (STDLIB/Structure)
                if res.returncode != 0 and "NameError" in res.stderr:
                    match = re.search(r"name '(\w+)' is not defined", res.stderr)
                    if match:
                        missing_var = match.group(1)
                        # Heuristic: If it looks like a package (all lowercase, no underscores), try importing it
                        if missing_var.islower() and "_" not in missing_var:
                            status_ph.markdown(render_hud(f"HEALING: INJECTING IMPORT {missing_var.upper()}...", 60 + (attempt*10), "#ef4444"), unsafe_allow_html=True)
                            code = f"import {missing_var}\n{code}"
                            with open(exec_path, "w", encoding='utf-8') as f: f.write(code)
                            attempt += 1
                            continue # RETRY LOOP

                return {"success": res.returncode==0, "stdout": res.stdout, "stderr": res.stderr, "code": code}
                
            except subprocess.TimeoutExpired:
                return {"success": False, "stdout": "", "stderr": "TIMEOUT: Execution exceeded 45s.", "code": code}
            except Exception as e:
                return {"success": False, "stdout": "", "stderr": str(e), "code": code}
        
        return {"success": False, "stdout": "", "stderr": "Max retries exceeded during self-healing.", "code": code}

# --- D. PLATINUM DASHBOARD ---

st.markdown("<h1 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 20px; margin-bottom: 30px;'>OUROBOROS <span style='color:#3b82f6'>INVICTUS</span></h1>", unsafe_allow_html=True)

# STATE
if "prompt" not in st.session_state: st.session_state.prompt = ""
if "page" not in st.session_state: st.session_state.page = "Builder"

# SIDEBAR
with st.sidebar:
    st.markdown("### 🔐 ACCESS")
    api_key = st.text_input("Enter Key", type="password", value="AIzaSyBHcbC33_CzOtTXXuYlj7Lq3TAIzLmgvbU")
    
    st.markdown("### 🛠️ WORKBENCH")
    page = sac.menu([
        sac.MenuItem('Code Builder', icon='code-square', description='Generate New Tools'),
        sac.MenuItem('Code Surgeon', icon='bandaid', description='Repair Broken Scripts'),
    ], size='md', variant='filled', color='blue', index=0 if st.session_state.page == "Builder" else 1)
    
    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()
        
    st.divider()
    if st.button("⚠️ HARD RESET SYSTEM", use_container_width=True):
        st.session_state.clear()
        clean_artifacts()
        st.rerun()
        
    st.markdown("### 🚦 STATUS")
    st.success("SYSTEM ONLINE (INVICTUS V34 TURBO)")

try:
    # 1. BUILDER MODE
    if st.session_state.page == 'Code Builder':
        c1, c2 = st.columns([3, 1])
        with c2:
            st.write("### ⚡ Quick Ops")
            def set_p(t): st.session_state.prompt = t
            
            if st.button("Simulate Snake 🐍", use_container_width=True):
                set_p("Write a Python script to simulate a Snake Game logic (no GUI, no pygame). Run 50 moves on a 20x20 grid. Snake body is a list of (x, y) tuples. Store path. Visualize with Matplotlib (scatter plot). Save as 'snake_game.png'. Print 'Game Over'.")
                st.rerun()
            if st.button("Draw 3D Spiral 🌀", use_container_width=True):
                set_p("Write a Python script using 'matplotlib' and 'numpy'. Generate a dataset for a 3D Helix (Spiral). Plot it using `ax.scatter`. Use a 'viridis' colormap. Save the figure as 'spiral_3d.png'. Do NOT use plt.show(). Print 'Spiral Generated'.")
                st.rerun()
            if st.button("Generate QR Code 📱", use_container_width=True):
                set_p("Write a Python script using the 'qrcode' library. Generate a QR code for the URL 'https://ouroboros.streamlit.app'. Save it as 'my_qr.png'. Print 'QR Code Saved'.")
                st.rerun()

        with c1:
            st.write("### 📝 Directives")
            u_input = st.text_area("Builder Input", value=st.session_state.prompt, height=200, placeholder="Describe the software you want to build...")
            run_build = st.button("INITIALIZE BUILD", type="primary", use_container_width=True)

    # 2. SURGEON MODE
    elif st.session_state.page == 'Code Surgeon':
        st.write("### 🚑 Operations Table")
        u_input = st.text_area("Paste Broken Code", height=150, placeholder="# Paste code here...")
        err_input = st.text_area("Paste Error Message", height=80, placeholder="TypeError: ...")
        run_build = st.button("INITIALIZE REPAIR", type="primary", use_container_width=True)

    # --- E. EXECUTION POOL ---
    def render_hud(phase, pct, color="#3b82f6"):
        return f"""
        <div class="hud-card">
            <div style="color:{color}; font-weight:600; font-family:'Inter'; letter-spacing:1px;">
                {phase}
            </div>
            <div class="hud-progress-track">
                <div class="hud-progress-bar" style="width: {pct}%; background:{color};"></div>
            </div>
        </div>
        """

    if run_build and u_input:
        if not api_key: st.error("Authentication Missing")
        else:
            eng = InvictusEngine(api_key)
            ph = st.empty()
            
            # 1. ARCHITECTING (TITANIUM LOOP -> DIAMOND DISCOVERY)
            ph.markdown(render_hud("INITIATING INVICTUS CORE...", 20), unsafe_allow_html=True)
            
            reflexion_attempts = 0
            max_reflexion = 5 # V30 OMEGA: Max Retries
            last_error_context = err_input if st.session_state.page == 'Code Surgeon' else None
            last_code_attempt = "" # Track code to feed back
            
            while reflexion_attempts <= max_reflexion:
                # GENERATE
                if reflexion_attempts > 0:
                     ph.markdown(render_hud(f"🧠 REFLEXION ({reflexion_attempts}/{max_reflexion}): FIXING LOGIC...", 40, "#ec4899"), unsafe_allow_html=True)
                     # V25 RECURSIVE REPAIR: Feed the BROKEN CODE back to the AI
                     # "Here is the code you wrote, it failed with this error. Fix it."
                     current_prompt = (
                         f"You wrote this code:\n{last_code_attempt}\n\n"
                         f"It failed with this error:\n{last_error_context}\n\n"
                         f"FIX THE CODE."
                     )
                     mode = "surgeon" 
                else:
                     current_prompt = u_input
                     mode = "surgeon" if st.session_state.page == 'Code Surgeon' else "architect"

                code = eng.generate(current_prompt, mode=mode, error_context=last_error_context, status_ph=ph)
                last_code_attempt = code # Save for next loop if needed
                time.sleep(0.3)
                
                # 2. COMPILING (SELF-HEALING)
                ph.markdown(render_hud("COMPILING ASSETS...", 50, "#fbbf24"), unsafe_allow_html=True)
                res = eng.execute_with_healing(code, ph)
                
                # V26 LOUDMOUTH CHECK: Detect Silent Failure
                found_artifacts = []
                for ext in ["*.png", "*.jpg", "*.jpeg", ".svg"]:
                    found_artifacts.extend(glob.glob(ext))
                
                has_output = bool(res['stdout'].strip()) or bool(found_artifacts)
                
                if res['success'] and has_output:
                    break # success and loud!
                elif res['success'] and not has_output:
                     # SILENT FAILURE -> Force Reflexion
                     last_error_context = "RUNTIME ERROR: SILENT FAILURE. The code ran successfully but produced NO OUTPUT (no print statements, no images). You MUST use print() to show the result."
                     reflexion_attempts += 1
                else:
                    # Standard Failure
                    last_error_context = res['stderr']
                    with st.expander("🛑 Error Logs (Debug)", expanded=True):
                        st.code(res['stderr'], language="text")
                    reflexion_attempts += 1
            
            # 3. VERIFYING
            
            # 3. VERIFYING
            ph.markdown(render_hud("VERIFICATION COMPLETE", 100, "#10b981"), unsafe_allow_html=True)
            time.sleep(0.5)
            
            # --- F. RESULTS DECK ---
            st.write("### 📡 Mission Report")
            
            t1, t2, t3 = st.tabs(["Output View", "Terminal Stream", "Source Code"])
            
            with t1:
                # CHECK FOR RATE LIMIT WARNING
                if "429" in res['stdout'] or "429" in res['stderr']:
                    st.warning("⚠️ QUOTA EXCEEDED (429): Google Gemini API rate limit reached. Please wait a moment or check your billing.")
                
                # UNIVERSAL VISUALIZER
                images = []
                for ext in ["*.png", "*.jpg", "*.jpeg", ".svg"]:
                    images.extend(glob.glob(ext))
                
                if images:
                    st.info(f"Visual Artifacts Detected: {len(images)}")
                    cols = st.columns(len(images)) if len(images) < 4 else st.columns(3)
                    for i, img_path in enumerate(images):
                        with cols[i % len(cols)]:
                            st.image(img_path, caption=img_path, use_column_width=True)
                
                if res['stdout'].strip():
                    st.markdown(f"<div class='terminal-card'>{res['stdout']}</div>", unsafe_allow_html=True)
                    
                if not images and not res['stdout'].strip():
                    if res['stderr']:
                        st.markdown(f"<div class='terminal-card error-card'>RUNTIME_ERROR:\n{res['stderr']}</div>", unsafe_allow_html=True)
                    else:
                        st.info("Program completed silently.")

            with t2:
                st.text_area("Full Stderr", value=res['stderr'], height=200)
                
            with t3:
                st.code(res['code'], language='python')
                
except Exception as e:
    st.error(f"CRITICAL SYSTEM FAILURE: {str(e)}")
