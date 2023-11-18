from enum import Enum

class AutoGluonParameter(Enum):
    # Predictor parameters
    PROBLEM_TYPE = 'classification'
    EVAL_METRIC = 'accuracy'

    # Fit parameters
    PRESETS = 'best_quality'