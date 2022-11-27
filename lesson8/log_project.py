import logging
import logging.handlers

def init_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter("%(name)s ::: %(asctime)s ::: %(levelname)s ::: %(message)s")

    fh = logging.handlers.RotatingFileHandler(filename='logs/log.log', maxBytes=5000, backupCount=8, encoding='utf-8')
    fh.setFormatter(formatter)
    fh.setLevel(level)
    logger.addHandler(fh)
    logger.debug("logger init")
