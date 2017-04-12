import logging

class Configuration:
    learning_rate = 0.0005
    training_iters = 200000
    batch_size = 128
    display_step = 1
    dropout = 0.5
    test_number = 5000  # number of test images (out of 250000)

    CHECKPOINT_PATH = './results1/'
    TRAIN_FOLDER = './preprocessed'
    SUBMISSION_FOLDER = './test64'
    RESULT_FILE_PATH = CHECKPOINT_PATH + 'results.dat'

    LOGGER_NAME = 'main_logger'

    def __init__(self):
        pass

    @staticmethod
    def configure_logger():
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
