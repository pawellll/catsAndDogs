from Utils import Utils
import logging

class Configuration:
    learning_rate = 0.0005
    epochs = 10
    batch_size = 128
    display_step = 1
    dropout = 0.5

    CHECKPOINT_PATH = './result6_augmented5000/'
    # TRAIN_FOLDER = './augmented'
    # TRAIN_FOLDER = './preprocessed'
    # TRAIN_FOLDER = './reduced_10000'
    # TRAIN_FOLDER = './reduced_5000'
    TRAIN_FOLDER = './augmented_5000'
    SUBMISSION_FOLDER = './test64'
    VERIFICATION_FOLDER = './verification64'
    RESULT_FILE_PATH = CHECKPOINT_PATH + 'results.dat'

    LOGGER_NAME = 'main_logger'

    def __init__(self):
        pass

    @staticmethod
    def maybe_create_result_folder():
        Utils.maybe_create_directory(Configuration.CHECKPOINT_PATH)

    @staticmethod
    def configure_logger():

        Configuration.maybe_create_result_folder()

        logger = logging.getLogger(Configuration.LOGGER_NAME)
        logger.setLevel(logging.DEBUG)

        sh = logging.StreamHandler()
        fh = logging.FileHandler(Configuration.RESULT_FILE_PATH)

        sh.setLevel(logging.DEBUG)
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')

        # add formatter to sh
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(sh)
        logger.addHandler(fh)

        logger.info("Logger configured")

    @staticmethod
    def save_config():
        logger = logging.getLogger(Configuration.LOGGER_NAME)
        logger.info("Saving configuration")

        with open(Configuration.CHECKPOINT_PATH + "config.txt", 'w') as f:
            f.write(str(Configuration.__dict__)) 
