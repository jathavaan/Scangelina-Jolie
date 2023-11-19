from enum import Enum


class AutoGluonParameter(Enum):
    # Predictor parameters
    PROBLEM_TYPE = 'multiclass'
    EVAL_METRIC = 'accuracy'
    VERBOSITY: int = 0

    # Fit parameters
    PRESETS = 'best_quality'
    AUTO_STACK: bool = True     # If True -> longer training times, but better results
    NUM_BAG_FOLDS: int = 5      # Recommended value [5, 10]
    NUM_BAG_SETS: int = 20      # Recommended value [1, 20]
    NUM_STACK_LEVELS: int = 1   # Recommended value [1, 3]
