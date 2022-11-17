import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


import utils
import constants


def examine_exercise_hr(start_date, end_date):
    exercises_dict = utils.read_exercise_data(start_date=start_date,
                                              end_date=end_date,
                                              exercise_type=constants.FUNCTIONAL_TRAINING)

    number_of_exercise_sessions = len(exercises_dict[constants.DATE_TIME])

    trainer_list = ['Trainer-1' if t.weekday() in [1, 3] else 'Trainer-2' for t in exercises_dict[constants.DATE_TIME]]

    start_d = datetime.datetime.fromisoformat(start_date)

    box_positions = [(t - start_d).total_seconds() / 86400 for t in exercises_dict[constants.DATE_TIME]]
    box_labels = [t.strftime('%Y-%m-%d -- %H:%M') for t in exercises_dict[constants.DATE_TIME]]

    hr_max = exercises_dict[constants.HR_MAX].reshape(1, -1)
    hr_min = exercises_dict[constants.HR_MIN].reshape(1, -1)
    hr_avg = exercises_dict[constants.HR_AVG].reshape(1, -1)

    plt.figure(figsize=(18, 8))
    plt.boxplot(x=exercises_dict[constants.HR], positions=box_positions)
    plt.xticks(rotation=45, labels=box_labels, ticks=box_positions)
    plt.show()

    plt.figure(figsize=(18, 8))
    y_err = np.concatenate((hr_avg - hr_min, hr_max - hr_avg))
    plt.errorbar(x=box_positions, y=hr_avg.reshape(number_of_exercise_sessions,), yerr=y_err, fmt='Db', capsize=3)
    plt.xticks(rotation=45, labels=box_labels, ticks=box_positions)
    plt.ylim((0, 220))
    plt.grid(visible=True)
    plt.title('Heart Rate: Average, Min, Max')
    plt.show()

    dummy = -32






    for i in range(number_of_exercise_sessions):

        hr_sampling_times = exercises_dict[constants.HR_SAMPLING_TIMES][i]
        hr = exercises_dict[constants.HR][i]
        is_measured = exercises_dict[constants.HR_IS_MEASURED][i]
        is_interpolated = np.logical_not(is_measured)

        plt.figure(figsize=(18, 8))
        plt.scatter(x=hr_sampling_times[is_measured], y=hr[is_measured], c='b', label='measured')
        plt.scatter(x=hr_sampling_times[is_interpolated], y=hr[is_interpolated], c='r', label='interpolated')

        plt.title(box_labels[i])
        plt.grid(visible=True)
        plt.legend()
        plt.show()

    dummy = -32
