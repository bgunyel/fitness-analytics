import datetime

import pandas as pd
import numpy as np

import constants
import utils


def compute_session_trimp(hr_avg, hr_max, hr_rest, duration_in_minutes, sex):

    fhrr = (hr_avg - hr_rest) / (hr_max - hr_rest)

    if sex == constants.MALE:
        coeff = 0.64 * np.exp(1.92 * fhrr)
    elif sex == constants.FEMALE:
        coeff = 0.86 * np.exp(1.67 * fhrr)
    else:
        raise Exception(f'Sex should be {constants.MALE} or {constants.FEMALE}')

    trimp = duration_in_minutes * coeff * fhrr
    return trimp


def compute_cumulative_fitness(exercise_dict, start_date, end_date):

    k1 = 1
    k2 = 1.5

    tau1 = 28
    tau2 = 7

    start_d = datetime.date.fromisoformat(start_date)
    end_d = datetime.date.fromisoformat(end_date)

    number_of_exercise_sessions = len(exercise_dict[constants.DATE_TIME])
    days = utils.generate_date_vector(start_d=start_d, end_d=end_d, out_format=constants.DATE)
    number_of_days = len(days)

    w = dict(zip(days, np.zeros(number_of_days)))

    for i in range(number_of_exercise_sessions):

        session_load = compute_session_trimp(hr_avg=exercise_dict[constants.HR_AVG][i],
                                             hr_max=exercise_dict[constants.HR_MAX][i],
                                             hr_rest=exercise_dict[constants.HR_REST][i],
                                             duration_in_minutes=exercise_dict[constants.DURATION][i]/60,
                                             sex=exercise_dict[constants.SEX])
        session_date = exercise_dict[constants.DATE_TIME][i].date()
        w[session_date] += session_load

    training_load = dict(zip(days, np.zeros(number_of_days)))
    fatigue = dict(zip(days, np.zeros(number_of_days)))
    fitness = dict(zip(days, np.zeros(number_of_days)))

    training_load[start_d] = w[start_d] * k1
    fatigue[start_d] = w[start_d] * k2
    fitness[start_d] = training_load[start_d] - fatigue[start_d]

    for idx, d in enumerate(days[1:]):
        training_load[d] = training_load[days[idx]] * np.exp(-1 / tau1) + w[d] * k1
        fatigue[d] = fatigue[days[idx]] * np.exp(-1 / tau2) + w[d] * k2
        fitness[d] = training_load[d] - fatigue[d]

    return training_load, fatigue, fitness

