#!/usr/bin/env python3
"""Main experiment runner script."""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.experiment import ExperimentRunner
import yaml

def load_config():
    """Load experiment configuration."""
    with open('configs/default_config.yaml', 'r') as f:
        return yaml.safe_load(f)

def main():
    """Run the experiment."""
    print("🚀 Starting experiment...")
    
    config = load_config()
    runner = ExperimentRunner(config)
    
    try:
        results = runner.run()
        print("✅ Experiment completed successfully")
        print(f"Results: {results}")
    except Exception as e:
        print(f"❌ Experiment failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 