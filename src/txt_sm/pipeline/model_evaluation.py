from txt_sm.config.configuration import Configuration_Manager
from txt_sm.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()