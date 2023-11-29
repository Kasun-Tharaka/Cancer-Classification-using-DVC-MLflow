from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.component.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingedestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zp_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************\n")
    except Exception as e:
        logger.exception(e)
        raise e