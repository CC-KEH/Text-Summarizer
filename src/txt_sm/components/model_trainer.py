from transformers import Trainer,TrainingArguments
from datasets import load_from_disk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from transformers import DataCollatorForSeq2Seq
from src.txt_sm.entity.config_entity import Model_Trainer_Config
import os

class Model_Trainer:
    def __init__(self,config:Model_Trainer_Config):
        self.config = config
    
    def initiate_model_trainer(self):
       device = 'cuda' if torch.cuda.is_available() else 'cpu'
       tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
       model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
       seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer,model=model_pegasus)
       
       dataset_pt = load_from_disk(self.config.data_path)
       
       training_args = TrainingArguments(
           output_dir=self.config.root_dir,
           num_train_epochs=self.config.num_train_epochs, 
           warmup_steps=self.config.warmup_steps, 
           per_device_train_batch_size=self.config.per_device_train_batch_size, 
           per_device_eval_batch_size=self.config.per_device_eval_batch_size, 
           weight_decay=self.config.weight_decay, 
           logging_steps=self.config.logging_steps, 
           evaluation_strategy=self.config.evaluation_strategy, 
           eval_steps=self.config.eval_steps, 
           save_steps=self.config.save_steps, 
           gradient_accumulation_steps=self.config.gradient_accumulation_steps
       )
       
       trainer = Trainer(model=model_pegasus,
                         args=training_args,
                         tokenizer=tokenizer,
                         data_collator=seq2seq_data_collator,
                         train_dataset=dataset_pt['train'],
                         eval_dataset=dataset_pt['validation'])
       
       trainer.train()
       
       model_pegasus.save_pretrained(os.path.join(self.config.root_dir,'pegasus-samsum-model'))
       
       tokenizer.save_pretrained(os.path.join(self.config.root_dir,'tokenizer'))