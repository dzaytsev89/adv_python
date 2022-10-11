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


def logger_to_spec_file(program):
    path = input('Укажите путь для файла логирования: ')
    if path == '':
        path = '.'
    elif not os.path.exists(path):
        os.makedirs(path)
    file = input('Имя файла логирования: ')
    if file == '':
        file = 'logger'
    def new_program(*args, **kwargs):
        result = program(*args, **kwargs)
        with open(path+'/'+file+'.txt', 'a', encoding='utf8') as log:
            log.write(f'{datetime.datetime.now()}: Function {program.__name__} called with params:'
                      f' {args},{kwargs} and have result: {result}\n')
        return result
    return new_program
