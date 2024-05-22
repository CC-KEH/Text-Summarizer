from src.txt_sm.logging import logger
from src.txt_sm.entity.config_entity import Data_Validation_Config
import os

class DataValidation:
    def __init__(self,config:Data_Validation_Config ):
        self.config = config

    def initiate_data_validation(self):
        try:
            validation_status = False
            all_files = os.listdir(os.path.join('artifacts','data_ingestion','data'))
            
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as file:
                        file.write(f'Validation status: {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as file:
                        file.write(f'Validation status: {validation_status}')
            
            if not validation_status:
                logger.info('Couldnt Validate all files')
            else:
                logger.info('Successfully Validated all files')
            
            return validation_status            
        
        except Exception as e:
            raise e