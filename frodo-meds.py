"""
    frodo-meds.py
    
    This nomograph relates the amount of medicine I have in stock for my cat with dose rates. This
    code was adapted from: http://lefakkomies.github.io/pynomo-doc/examples/examples.html

    This is a type 2 nomogram (F1 = F2*F3)

    F1 = mL   gabapentin in stock
    F2 = mL/d total dose per day
    F3 = d    number of days at this rate
"""

from pynomo.nomographer import *
import sys
sys.path.insert(0, "..")

N_params_1 = {
    'u_min': 0.00,
    'u_max': 8.0,
    'function': lambda u: u,
    'title': r'$mL$ in stock',
    'tick_levels': 3,
    'tick_text_levels': 1,
}

N_params_2 = {
    'u_min': 0.05,
    'u_max': 0.50,
    'function': lambda u: u,
    'title': r'$mL\over d$',
    'tick_levels': 3,
    'tick_text_levels': 2,
}

N_params_3 = {
    'u_min': 0.0,
    'u_max': 30.0,
    'function': lambda u: u,
    'title': r'$d$ days',
    'tick_levels': 2,
    'tick_text_levels': 1,
}


block_1_params = {
    'block_type': 'type_2',
    'width': 10.0,
    'height': 10.0,
    'f1_params': N_params_1,
    'f2_params': N_params_2,
    'f3_params': N_params_3,
    'isopleth_values': [
        [6, 0.35, 'x'],     # How many days to deplete a new stock of 6 mL
        ['x', 0.35, 3]      # How many mL is left when I have 3 days left to re-stock
    ],
}

main_params = {
    'filename': 'frodo-meds.pdf',
    'paper_height': 10.0,
    'paper_width': 10.0,
    'block_params': [block_1_params],
    'title_str': r'Frodo - gabapentin stock',
    'isopleth_params': [
        {'color': 'MidnightBlue', 'transparency': 0.2},
        {'color': 'Red', 'transparency': 0.2}
     ]
}

Nomographer(main_params)
