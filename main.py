import datetime

import matplotlib.pyplot as plt

import constants
import utils
import stats
import fitness
import guru


def development():
    start_date = '2022-04-01'
    end_date = '2022-11-30'

    # stats.examine_fitness_and_fatigue(start_date=start_date, end_date=end_date)
    guru.get_guru()



    dummy = -32

    # stats.examine_vo2max(start_date=start_date, end_date=end_date)
    # stats.examine_exercise_hr(start_date=start_date, end_date=end_date)


def main(params):
    print(params['name'])
    development()


if __name__ == '__main__':
    parameters = {'name': 'Fitness Analytics'}

    print('------------------')
    print(f'STARTED EXECUTION @ {datetime.datetime.now()}')
    print('------------------')

    main(params=parameters)

    print('------------------')
    print(f'FINISHED EXECUTION @ {datetime.datetime.now()}')
    print('------------------')
