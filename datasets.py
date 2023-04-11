
import numpy as np
import pandas as pd


def make_blood_pressure_df(reading_num):
    return pd.DataFrame({
        'MEMBER': members,
        f'BLOOD_PRESSURE_{reading_num}': np.random.randint(65, 120, len(members))
    })


members = 'Vi,Tyler,Kevin,Jillian,David'.split(',')

ages = pd.DataFrame({
    'MEMBER': members,
    'AGE': np.random.randint(25, 50, len(members))
})
bp1, bp2, bp3, bp4, bp5, bp6 = [make_blood_pressure_df(i + 1) for i in range(6)]

blood_pressures = pd.concat([
    df.rename(columns={f'BLOOD_PRESSURE_{i}': 'BLOOD_PRESSURE'})
    for i, df in enumerate([bp1, bp2, bp3, bp4, bp5, bp6], 1)
])
