from src.Datascience.config.configuration import ConfigurationManager
from src.Datascience.components.moder_trainer import Model_trainer
from src.Datascience import logger



STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = Model_trainer(config=model_trainer_config)
        model_trainer_config.train()