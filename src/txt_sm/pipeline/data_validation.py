from txt_sm.config.configuration import Configuration_Manager
from txt_sm.components.data_validation import DataValiadtion


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()