from typing import Final

DATA_FOLDER: Final = './data/'
OUT_FOLDER: Final = './out/'

POLAR_DATA_FOLDER: Final = DATA_FOLDER + 'polar_bg/'
GURU_ENV_FILE: Final = './guru_env.json'
GURU_TOKEN_FILE: Final = './guru_token.json'

WANDB_PROJECT_NAME: Final = 'todo-todo'
WANDB_USER_NAME: Final = 'bertan-gunyel'
WANDB_DYNAMIC_VIS: Final = 'dynamic-vis'
WANDB_STATIC_VIS: Final = 'static-vis'

WANDB_TODO_TODO_TABLE: Final = 'todo-todo-table'

ATHLETE: Final = 'athlete'
SEX: Final = 'sex'
DATE_TIME: Final = 'date_time'
DISTANCE: Final = 'distance (m)'
ELAPSED_TIME: Final = 'elapsed_time (s)'
ELEVATION_GAIN: Final = 'elevation_gain (m)'
AVERAGE_HEART_RATE: Final = 'average_heart_rate (bpm)'
SLOPE: Final = 'slope'
SPEED: Final = 'speed (min/km)'  # raw speed
ADJUSTED_SPEED: Final = 'adjusted_speed'

MALE: Final = 'MALE'
FEMALE: Final = 'FEMALE'

FUNCTIONAL_TRAINING: Final = 'FUNCTIONAL_TRAINING'
STRENGTH_TRAINING: Final = 'STRENGTH_TRAINING'
RUNNING: Final = 'RUNNING'
HIIT: Final = 'HIIT'

DURATION: Final = 'duration'
EXERCISE_TYPE: Final = 'exercise_type'
PHYSICAL_INFORMATION_SNAPSHOT: Final = 'physicalInformationSnapshot'
MAX_HEART_RATE: Final = 'maximumHeartRate'
RESTING_HEART_RATE: Final = 'restingHeartRate'
AEROBIC_THRESHOLD: Final = 'aerobicThreshold'
ANAEROBIC_THRESHOLD: Final = 'anaerobicThreshold'
VO2_MAX: Final = 'vo2Max'


LATITUDE: Final = 'latitude'
LONGITUDE: Final = 'longitude'
ELEVATION: Final = 'elevation'
HR: Final = 'hr'  # heart rate
CAD: Final = 'cad'  # cadence
HR_SAMPLING_TIMES: Final = 'hr_sampling_times'
HR_IS_MEASURED: Final = 'hr_is_measured'
HR_MAX: Final = 'hr_max'
HR_REST: Final = 'hr_rest'
HR_AVG: Final = 'hr_avg'

GREAT_CIRCLE: Final = 'great_circle_distance'
GEODESIC: Final = 'geodesic_distance'
EUCLIDEAN_GREAT_CIRCLE: Final = 'euclidean_great_circle'
EUCLIDEAN_GEODESIC: Final = 'euclidean_geodesic'

DATE: Final = 'date'
TIME: Final = 'time'
YEAR: Final = 'year'
MONTH: Final = 'month'
DAY: Final = 'day'  # day in the month
WEEK_DAY: Final = 'week_day'
WEEKEND: Final = 'weekend'
HOUR: Final = 'hour'
QUARTER: Final = 'quarter'

START_TIME: Final = 'startTime'
STOP_TIME: Final = 'stopTime'

MONDAY: Final = 'Monday'
TUESDAY: Final = 'Tuesday'
WEDNESDAY: Final = 'Wednesday'
THURSDAY: Final = 'Thursday'
FRIDAY: Final = 'Friday'
SATURDAY: Final = 'Saturday'
SUNDAY: Final = 'Sunday'

MEN: Final = 'men'
WOMEN: Final = 'women'
RECORD: Final = 'record'

WORLD_RECORD_SPEEDS: Final = {DISTANCE: [1000, 1500, 1609.344, 2000, 3218.688, 5000, 10000, 21097.5, 42195],
                              MEN: [2.20, 2.29, 2.31, 2.38, 2.48, 2.52, 2.62, 2.73, 2.87],
                              WOMEN: [2.48, 2.56, 2.61, 2.71, 2.79, 2.82, 2.93, 2.98, 3.18]}

list_colors = ["#00FF00",
               "#12FF00",
               "#24FF00",
               "#35FF00",
               "#47FF00",
               "#58FF00",
               "#6AFF00",
               "#7CFF00",
               "#8DFF00",
               "#9FFF00",
               "#B0FF00",
               "#C2FF00",
               "#D4FF00",
               "#E5FF00",
               "#F7FF00",
               "#FFF600",
               "#FFE400",
               "#FFD300",
               "#FFC100",
               "#FFAF00",
               "#FF9E00",
               "#FF8C00",
               "#FF7B00",
               "#FF6900",
               "#FF5700",
               "#FF4600",
               "#FF3400",
               "#FF2300",
               "#FF1100",
               "#FF0000"]
