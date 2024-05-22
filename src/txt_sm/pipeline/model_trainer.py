from txt_sm.config.configuration import Configuration_Manager
from txt_sm.components.model_trainer import ModelTrainer


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()