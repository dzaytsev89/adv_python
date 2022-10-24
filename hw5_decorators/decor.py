import datetime
import os


def logger(program):
    def new_program(*args, **kwargs):
        result = program(*args, **kwargs)
        with open('./logger.txt', 'a', encoding='utf8') as log:
            log.write(f'{datetime.datetime.now()}: Function {program.__name__} called with params:'
                      f' {args},{kwargs} and have result: {result}\n')
        return result
    return new_program


def logger_to_spec_file(log_file='./logger.txt'):
    print(os.path.dirname(log_file))
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    def logger(program):
        def new_program(*args, **kwargs):
            result = program(*args, **kwargs)
            with open(log_file, 'a', encoding='utf8') as log:
                log.write(f'{datetime.datetime.now()}: Function {program.__name__} called with params:'
                          f' {args},{kwargs} and have result: {result}\n')
            return result
        return new_program
    return logger
