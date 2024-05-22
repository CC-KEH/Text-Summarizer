from dataclasses import dataclass
from pathlib import Path 

@dataclass(frozen=True)
class Data_Ingestion_Config:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass(frozen=True)
class Data_Validation_Config:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list     


@dataclass(frozen=True)
class Data_Transformation_Config:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

    
@dataclass(frozen=True)
class Model_Trainer_Config:
    root_dir: Path
    model_path: Path
    data_path: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    
    
@dataclass(frozen=True)
class Model_Evaluation_Config:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path