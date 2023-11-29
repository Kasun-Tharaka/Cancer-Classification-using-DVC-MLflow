import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:

        try:
            dataset_url = self.config.source_url
            zip_dowload_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"downloading data from {dataset_url} into {zip_dowload_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_dowload_dir)

            logger.info(f"downloaded data from {dataset_url} into {zip_dowload_dir}")

        except Exception as e:
            raise e
        
    def extract_zp_file(self):
        unzip_data = self.config.unzip_dir
        os.makedirs(unzip_data, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_data)