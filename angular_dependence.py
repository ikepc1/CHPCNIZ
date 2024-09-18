import numpy as np

ANGLES = np.deg2rad(np.array([0., 5., 10., 15., 20., 25., 30., 35., 40., 41., 42., 43.]))
FRACTIONS = np.array([1., .993, .981, .968, .968, .942, .944, .901, .434, .221, .074, .009])
#FRACTIONS = np.array([1.,.993,.981, .968, .968, .942, .944*0.74378388, .901*0.63423332, .434*0.63423332, .221*.5, .074, .009])


def filter(angles: np.ndarray) -> np.ndarray:
    '''This function interpolates in Omura's simulated angular response.
    '''
    return np.interp(angles, ANGLES, FRACTIONS)
