from application import salary
from application.db import people
import datetime
from py_youtube import Search

if __name__ == '__main__':
    print('Текущая дата', datetime.date.today())
    people.get_employees()
    salary.calculate_salary(115)
    videos = Search('Techic').videos()
    print(videos)
