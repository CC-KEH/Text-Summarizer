from txt_sm.config.configuration import Configuration_Manager
from txt_sm.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()