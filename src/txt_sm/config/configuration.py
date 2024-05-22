from src.txt_sm.constants import *
from src.txt_sm.utils.common import read_yaml,create_dirs
from src.txt_sm.entity import (Data_Ingestion_Config,
                               Data_Transformation_Config,
                               Data_Validation_Config,
                               Model_Trainer_Config,
                               Model_Evaluation_Config)

class Configuration_Manager:
    def __init__(self,config_path=CONFIG_PATH,params_path=PARAMS_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        create_dirs([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> Data_Ingestion_Config:
        config = self.config
        
        create_dirs([config.root_dir])
        data_ingestion_config = Data_Ingestion_Config(root_dir=config.root_dir,
                                                      source_URL=config.source_URL,
                                                      local_data_file=config.local_data_file,
                                                      unzip_dir=config.unzip_dir)
        return data_ingestion_config

    def get_data_validation_config(self) -> Data_Validation_Config:
        config = self.config
        
        create_dirs([config.root_dir])
        data_validation_config = Data_Validation_Config(root_dir=config.root_dir,
                                                      STATUS_FILE=config.STATUS_FILE,
                                                      ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES)
        return data_validation_config
    
    def get_data_transformation_config(self) -> Data_Transformation_Config:
        config = self.config.data_transformation

        create_dirs([config.root_dir])

        data_transformation_config = Data_Transformation_Config(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> Model_Trainer_Config:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_dirs([config.root_dir])

        model_trainer_config = Model_Trainer_Config(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.evaluation_strategy,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> Model_Evaluation_Config:
        config = self.config.model_evaluation

        Model_Evaluation_Config([config.root_dir])

        model_evaluation_config = Model_Evaluation_Config(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )

        return model_evaluation_config