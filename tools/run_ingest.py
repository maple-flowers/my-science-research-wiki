#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unified Update Workflow for Research Wiki.
Mechanical Stage: Asset Sync and Writing Ingest.
"""

import subprocess
import sys
import time
from pathlib import Path

# Paths configuration
TOOLS_DIR = Path(__file__).parent
BASE_DIR = TOOLS_DIR.parent

def log(step, msg):
    timestamp = time.strftime("%H:%M:%S")
    try:
        output = f"[{timestamp}] [{step}] {msg}"
        sys.stdout.buffer.write((output + "\n").encode('utf-8'))
        sys.stdout.flush()
    except Exception:
        try:
            print(f"[{timestamp}] [{step}] {msg.encode('ascii', 'replace').decode('ascii')}")
        except Exception:
            pass

def run_script(script_name, args=None):
    script_path = TOOLS_DIR / script_name
    if not script_path.exists():
        log("ERROR", f"Script not found: {script_name}")
        return False

    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)

    log("START", f"Running {script_name}...")
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=False, # Read bytes to avoid decoding issues at this level
            bufsize=1
        )

        for line in process.stdout:
            try:
                # Direct pipe of bytes to stdout if possible, or decode as utf-8 safely
                sys.stdout.buffer.write(b"  " + line)
                sys.stdout.flush()
            except Exception:
                pass

        process.wait()
        if process.returncode == 0:
            log("SUCCESS", f"Finished {script_name}")
            return True
        else:
            log("FAILED", f"{script_name} exited with code {process.returncode}")
            return False
    except Exception as e:
        log("ERROR", f"Exception running {script_name}: {e}")
        return False

def main():
    start_time = time.time()
    log("SYSTEM", "Starting Wiki Raw Ingest Workflow")
    log("SYSTEM", f"Base Directory: {BASE_DIR}")
    print("-" * 60)

    # Step 1: Raw Asset Sync (Figures, Tables, Formulas)
    if not run_script("update_raw_assets.py"):
        log("ERROR", "Raw asset sync failed.")
        sys.exit(1)

    print("-" * 60)
    duration = time.time() - start_time
    log("SYSTEM", f"Raw Ingest Complete! Total time: {duration:.2f} seconds")
    log("SYSTEM", "Next Step: Run '/workflow update_research_wiki' in Claude to intelligently update Wiki content (Concepts, Entities, Projects, Figures, and Writing).")

if __name__ == "__main__":
    main()
