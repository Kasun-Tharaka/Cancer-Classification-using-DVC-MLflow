from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.component.model_trainer import Training
from cnnClassifier import logger


STAGE_NAME = 'Training'

class ModelTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
        obj = ModelTrainigPipeline()
        obj.main()
        logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************\n")
    except Exception as e:
        logger.exception(e)
        raise e