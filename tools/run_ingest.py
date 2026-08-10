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
    print(f"[{timestamp}] [{step}] {msg}")

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
            text=True,
            encoding='utf-8',
            bufsize=1
        )

        for line in process.stdout:
            print(f"  {line.strip()}")

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
    # Step 2: Basic Writing Ingest (Yearly folders)
    if not run_script("generate_writing_wiki.py"):
        log("WARNING", "Writing summary ingest encountered issues.")

    print("-" * 60)
    duration = time.time() - start_time
    log("SYSTEM", f"Raw Ingest Complete! Total time: {duration:.2f} seconds")
    log("SYSTEM", "Next Step: Run '/workflow update_research_wiki' in Claude to intelligently update Wiki content.")

if __name__ == "__main__":
    main()
