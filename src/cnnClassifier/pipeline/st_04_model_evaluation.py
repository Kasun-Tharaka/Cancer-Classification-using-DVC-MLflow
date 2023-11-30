from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.component.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger


STAGE_NAME = 'Evaluation'

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        eval_config = Evaluation(config=eval_config)
        eval_config.evaluation()
        eval_config.save_score()
        # eval_config.log_into_mlflow() #comented just fast run of DVC.


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************\n")
    except Exception as e:
        logger.exception(e)
        raise e