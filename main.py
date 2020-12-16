# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="C:/workspace/python/logging/logs.log",
                        level=logging.DEBUG,
                        format=LOG_FORMAT,
                        filemode='w'
                        )
    logger = logging.getLogger()

    logger.info("This is an info message src=pfd, dag=my_dag, status=success")
    logger.info("This is another information message src=pfd, dag=my_dag")

    for i in range(10):
        logger.info("Some random information")
        logger.info("Other random information")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
