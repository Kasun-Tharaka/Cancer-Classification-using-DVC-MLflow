from cnnClassifier import logger
from cnnClassifier.pipeline.st_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.st_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingedestion Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"

try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************")
except Exception as e:
    logger.exception(e)
    raise e