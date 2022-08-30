def print_first_task_result(task):
    """
    this function is called automatically once the task is finished.
    ref: https://django-q.readthedocs.io/en/latest/tasks.html#hook
    """

    # print(task.result)
    print("waited for 10 seconds")


def print_second_task_result(task):
    print("waited for 5 seconds")
