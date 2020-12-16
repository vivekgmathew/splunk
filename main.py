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


    #logger.info("This is an info message pfd_src=pfd, pfd_dag=my_dag, pfd_dag_status=success")
    #logger.info("Task one of your_dag completed pfd_src=pfd, pfd_dag=your_dag, pfd_task=task_one, pfd_task_status=success")
    logger.info(
        "Task one of your_dag completed pfd_src=pfd, pfd_dag=new_dag, pfd_task=task_three, pfd_task_status=success")


    for i in range(10):
        logger.info("Some random information")
        logger.info("Other random information")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
