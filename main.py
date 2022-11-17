import datetime

import constants
import utils
import stats


def development():

    start_date = '2022-09-08'
    end_date = '2022-12-31'

    stats.examine_exercise_hr(start_date=start_date, end_date=end_date)



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