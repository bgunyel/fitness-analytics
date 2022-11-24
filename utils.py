import os
import json
import datetime

import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

import constants


def read_exercise_data(start_date, end_date, exercise_type=None):
    interpolation_type = 'linear'

    data_folder = constants.POLAR_DATA_FOLDER
    files = os.listdir(data_folder)
    files = [f for f in files if os.path.isfile(data_folder + '/' + f)]
    files.sort()

    start_d = datetime.date.fromisoformat(start_date)
    end_d = datetime.date.fromisoformat(end_date)

    hr_list = []  # heart rate samples for each exercise session
    hr_sample_times_list = []
    hr_is_measured_list = []

    hr_max_list = []
    hr_rest_list = []
    hr_avg_list = []

    date_time_list = []
    exercise_types_list = []
    exercise_durations_list = []

    vo2_max_list = []
    aerobic_threshold_list = []
    anaerobic_threshold_list = []
    # resting_hr_list = []


    for file_name in files:

        file_path = os.path.join(data_folder, file_name)
        f = open(file_path)
        data_dict = json.load(f)

        date_time = datetime.datetime.fromisoformat(data_dict[constants.START_TIME])
        date = date_time.date()

        if (date < start_d) or (date > end_d):
            f.close()
            continue

        for ex in data_dict['exercises']:
            ex_type = ex['sport']

            if (exercise_type is None) or (ex_type == exercise_type):
                start_time = datetime.datetime.fromisoformat(ex[constants.START_TIME])
                stop_time = datetime.datetime.fromisoformat(ex[constants.STOP_TIME])
                duration = stop_time - start_time

                hr_measured = np.array([x['value'] for x in ex['samples']['heartRate'] if 'value' in x.keys()])
                t_measured = np.array([(datetime.datetime.fromisoformat(x['dateTime']) - start_time).total_seconds() for x in
                              ex['samples']['heartRate'] if 'value' in x.keys()])
                t_interpolated = np.array([(datetime.datetime.fromisoformat(x['dateTime']) - start_time).total_seconds() for x in
                              ex['samples']['heartRate'] if 'value' not in x.keys()])

                f_interp = interp1d(t_measured, hr_measured, kind=interpolation_type, assume_sorted=True, fill_value='extrapolate')
                hr_interpolated = f_interp(t_interpolated)

                t = np.concatenate((t_measured, t_interpolated))
                hr = np.concatenate((hr_measured, hr_interpolated))
                is_measured = np.concatenate((np.ones(shape=t_measured.shape, dtype=bool),
                                              np.zeros(shape=t_interpolated.shape, dtype=bool)))

                idx = np.argsort(t)
                t = t[idx]
                hr = hr[idx]
                is_measured = is_measured[idx]


                date_time_list.append(start_time)

                hr_list.append(hr)
                hr_sample_times_list.append(t)
                hr_is_measured_list.append(is_measured)

                hr_max_list.append(data_dict[constants.PHYSICAL_INFORMATION_SNAPSHOT][constants.MAX_HEART_RATE])
                hr_rest_list.append(data_dict[constants.PHYSICAL_INFORMATION_SNAPSHOT][constants.RESTING_HEART_RATE])
                hr_avg_list.append(np.mean(hr))

                exercise_types_list.append(ex_type)
                exercise_durations_list.append(duration.total_seconds())

                aerobic_threshold_list.append(
                    data_dict[constants.PHYSICAL_INFORMATION_SNAPSHOT][constants.AEROBIC_THRESHOLD])
                anaerobic_threshold_list.append(
                    data_dict[constants.PHYSICAL_INFORMATION_SNAPSHOT][constants.ANAEROBIC_THRESHOLD])
                vo2_max_list.append(data_dict[constants.PHYSICAL_INFORMATION_SNAPSHOT][constants.VO2_MAX])

        # Closing file
        f.close()

    out_dict = {constants.DATE_TIME: date_time_list,
                constants.HR: hr_list,
                constants.HR_SAMPLING_TIMES: hr_sample_times_list,
                constants.HR_IS_MEASURED: hr_is_measured_list,
                constants.HR_MAX: np.array(hr_max_list),
                constants.HR_REST: np.array(hr_rest_list),
                constants.HR_AVG: np.array(hr_avg_list),
                constants.EXERCISE_TYPE: exercise_types_list,
                constants.DURATION: exercise_durations_list,
                constants.AEROBIC_THRESHOLD: aerobic_threshold_list,
                constants.ANAEROBIC_THRESHOLD: anaerobic_threshold_list,
                constants.VO2_MAX: vo2_max_list,
                constants.SEX: data_dict[constants.PHYSICAL_INFORMATION_SNAPSHOT][constants.SEX]}

    return out_dict


def clean_data(df):

    out_df = df.copy(deep=True)

    # TODO: Cleaning code here

    return out_df


def x_positions_and_labels_for_datetime(start_datetime, datetime_vector, labels_format):

    x_positions = [(t - start_datetime).total_seconds() / 86400 for t in datetime_vector]

    if labels_format == constants.DATE_TIME:
        x_labels = [t.strftime('%Y-%m-%d -- %H:%M') for t in datetime_vector]
    elif labels_format == constants.DATE:
        x_labels = [t.strftime('%Y-%m-%d') for t in datetime_vector]
    else:
        raise Exception('Unknown Labels Format!')

    return x_positions, x_labels


def generate_date_vector(start_d, end_d, out_format):
    number_of_days = (end_d - start_d).days + 1

    if out_format == constants.DATE:
        days = [start_d + datetime.timedelta(days=d) for d in range(number_of_days)]
    elif out_format == constants.DATE_TIME:
        start_date = datetime.datetime.fromisoformat(start_d.isoformat())
        days = [start_date + datetime.timedelta(days=d) for d in range(number_of_days)]
    else:
        raise Exception('Unknown Format!')



    return days
