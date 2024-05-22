from txt_sm.config.configuration import Configuration_Manager
from txt_sm.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()