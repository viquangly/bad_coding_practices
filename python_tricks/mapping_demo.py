
import pandas as pd

from datasets import blood_pressures


def state_abbrev_to_word_bad(abbrev: str) -> str:
    if abbrev == 'NY':
        return 'NEW YORK'
    elif abbrev == 'TX':
        return 'TEXAS'
    elif abbrev == 'VA':
        return 'VIRGINIA'
    elif abbrev == 'NJ':
        return 'NEW JERSEY'
    else:
        return "I DON'T KNOW"


def state_abbrev_to_word_good(abbrev: str) -> str:
    state_dict = {
        'NY': 'NEW YORK',
        'TX': 'TEXAS',
        'VA': 'VIRGINIA',
        'NJ': 'NEW JERSEY'
    }
    if abbrev not in state_dict:
        return "I DON'T KNOW"
    else:
        return state_dict[abbrev]


def state_abbrev_to_word_better(abbrev: str) -> str:
    state_dict = {
        'NY': 'NEW YORK',
        'TX': 'TEXAS',
        'VA': 'VIRGINIA',
        'NJ': 'NEW JERSEY'
    }
    return state_dict.get(abbrev, "I DON'T KNOW")


state_abbrev_to_word_bad('NY')
state_abbrev_to_word_good('NY')
state_abbrev_to_word_better('NY')

state_abbrev_to_word_bad('CA')
state_abbrev_to_word_good('CA')
state_abbrev_to_word_better('CA')


blood_pressures

max_blood_pressures = blood_pressures.groupby('MEMBER')['BLOOD_PRESSURE'].max()
max_blood_pressures = max_blood_pressures.reset_index()
max_blood_pressures = max_blood_pressures.rename(columns={'BLOOD_PRESSURE': 'MAX_BLOOD_PRESSURE'})
merged = pd.merge(blood_pressures, max_blood_pressures, on='MEMBER')

max_blood_pressures_dict = dict(blood_pressures.groupby('MEMBER')['BLOOD_PRESSURE'].max())
blood_pressures['MAX_BLOOD_PRESSURE'] = blood_pressures['MEMBER'].map(max_blood_pressures_dict)
blood_pressures
