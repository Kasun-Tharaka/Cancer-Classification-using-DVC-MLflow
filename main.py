from cnnClassifier import logger
from cnnClassifier.pipeline.st_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingedestion Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************")
except Exception as e:
    logger.exception(e)
    raise e