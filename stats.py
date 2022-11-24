import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import utils
import constants
import fitness


def examine_exercise_hr(start_date, end_date):
    exercises_dict = utils.read_exercise_data(start_date=start_date,
                                              end_date=end_date,
                                              exercise_type=constants.FUNCTIONAL_TRAINING)

    number_of_exercise_sessions = len(exercises_dict[constants.DATE_TIME])

    trainer_list = ['Trainer-1' if t.weekday() in [1, 3] else 'Trainer-2' for t in exercises_dict[constants.DATE_TIME]]

    start_d = datetime.datetime.fromisoformat(start_date)

    x_positions, x_labels = utils.x_positions_and_labels_for_datetime(start_datetime=start_d,
                                                                      datetime_vector=exercises_dict[constants.DATE_TIME],
                                                                      labels_format=constants.DATE_TIME)

    hr_max = exercises_dict[constants.HR_MAX].reshape(1, -1)
    hr_min = exercises_dict[constants.HR_MIN].reshape(1, -1)
    hr_avg = exercises_dict[constants.HR_AVG].reshape(1, -1)

    plt.figure(figsize=(18, 8))
    plt.boxplot(x=exercises_dict[constants.HR], positions=x_positions)
    plt.xticks(rotation=45, labels=x_labels, ticks=x_positions)
    plt.show()

    plt.figure(figsize=(18, 8))
    y_err = np.concatenate((hr_avg - hr_min, hr_max - hr_avg))
    plt.errorbar(x=x_positions, y=hr_avg.reshape(number_of_exercise_sessions,), yerr=y_err, fmt='Db', capsize=3)
    plt.xticks(rotation=45, labels=x_labels, ticks=x_positions)
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

        plt.title(x_labels[i])
        plt.grid(visible=True)
        plt.legend()
        plt.show()

    dummy = -32


def examine_vo2max(start_date, end_date):
    exercises_dict = utils.read_exercise_data(start_date=start_date,
                                              end_date=end_date)

    number_of_exercise_sessions = len(exercises_dict[constants.DATE_TIME])

    vo2max_list = exercises_dict[constants.VO2_MAX]

    x_positions, x_labels = \
        utils.x_positions_and_labels_for_datetime(start_datetime=datetime.datetime.fromisoformat(start_date),
                                                  datetime_vector=exercises_dict[constants.DATE_TIME],
                                                  labels_format=constants.DATE)

    plt.figure(figsize=(18, 8), layout='constrained')
    plt.scatter(x_positions, vo2max_list, marker='D')
    plt.xticks(rotation=90, labels=x_labels, ticks=x_positions)
    plt.title('VO2_max over time')
    plt.show()


def examine_fitness_and_fatigue(start_date, end_date):

    exercises_dict = utils.read_exercise_data(start_date=start_date, end_date=end_date)
    training_load, fatigue, fitness_vector = fitness.compute_cumulative_fitness(exercise_dict=exercises_dict,
                                                                                start_date=start_date,
                                                                                end_date=end_date)

    start_d = datetime.date.fromisoformat(start_date)
    end_d = datetime.date.fromisoformat(end_date)
    days = utils.generate_date_vector(start_d=start_d, end_d=end_d, out_format=constants.DATE_TIME)

    x_positions, x_labels = \
        utils.x_positions_and_labels_for_datetime(start_datetime=datetime.datetime.fromisoformat(start_date),
                                                  datetime_vector=days,
                                                  labels_format=constants.DATE)


    plt.figure(figsize=(18, 8))
    plt.plot(x_positions, fitness_vector.values(), marker='D', c='g', label='Fitness')
    plt.plot(x_positions, fatigue.values(), marker='o', c='r', label='Fatigue')
    plt.plot(x_positions, training_load.values(), marker='o', c='b', label='Training Load')
    plt.xticks(rotation=90, labels=x_labels, ticks=x_positions)
    plt.legend()
    plt.title('Training Load, Fatigue, and Fitness')
    plt.ylabel('AU (Arbitrary Unit)')
    plt.show()

    dummy = -32
