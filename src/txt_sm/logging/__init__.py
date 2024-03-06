import os,sys,logging

logging_str = ('[%(asctime)s: %(levelname)s: %(module)s: %(message)s]')

dir_name = 'logs'
file_name = 'running_logs.log'
log_file_path = os.path.join(dir_name,file_name)
os.makedirs(dir_name,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('TextSummarizerLogger')