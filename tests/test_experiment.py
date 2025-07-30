"""Tests for experiment runner."""

import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.experiment import ExperimentRunner

class TestExperimentRunner:
    
    @pytest.fixture
    def experiment_config(self):
        return {
            "experiment": {"name": "test_experiment", "seed": 42},
            "model": {"type": "basic"},
            "data": {"source": "data/input/"},
            "training": {"epochs": 10, "learning_rate": 0.001},
            "output": {"save_dir": "outputs/test/", "log_level": "INFO"}
        }
    
    def test_initialization(self, experiment_config):
        runner = ExperimentRunner(experiment_config)
        assert runner.config == experiment_config
        assert runner.results == {}
    
    def test_run_experiment(self, experiment_config):
        runner = ExperimentRunner(experiment_config)
        results = runner.run()
        assert results is not None
        assert "status" in results
        assert results["status"] == "completed" 