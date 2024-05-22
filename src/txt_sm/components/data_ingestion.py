import os
import urllib.request as request
import zipfile
from src.txt_sm.logging import logger
from src.txt_sm.utils.common import get_size
from src.txt_sm.entity.config_entity import Data_Ingestion_Config
from pathlib import Path 

class DataIngestion:
    def __init__(self,config:Data_Ingestion_Config):
        self.config = config

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as f:
            f.extractall(unzip_path)
                                                     
    def initiate_data_ingestion(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f'{filename} downloaded! with following info \n{headers}')
        else:
            logger.info(f'{filename} already exists! of size {get_size(Path(self.config.local_data_file))}')
        