# ARGUMENT PARSER AND MAIN USER INTERFACE 

import argparse

parser = argparse.ArgumentParser()


parser.add_argument('-s', '--states_dimension', type=int,
                    default=2, help='the number of states')
# dest='state_dim')

parser.add_argument('-o', '--output_dimension', type=int,
                    default=1, help='the number of outputs')
# dest='out_dim')

parser.add_argument('-i', '--input_dimension', type=int,
                    default=1, help='the number of control inputs')
# dest='input_dim')

parser.add_argument('-m', '--measured_dimension', type=int,
                    default=-1, help='the number of measured quantities')
# metavar='meas_dim')

parser.add_argument("-mech", "--mechanical", action="store_true",
                    help="the system to control is mechanical")

parser.add_argument("-p", "--planner", action="store_true",
                    help="add the local planner to control unit")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()

# TODO 
# add auxiliarry measurements parser 


STATE_DIM = args.states_dimension
OUTPUT_DIM = args.output_dimension
INPUT_DIM = args.input_dimension
MEASUREMENTS_DIM = args.measured_dimension
# USER_INPUTS_DIM = 2


def add_variable(name='var',
                 var_type='double',
                 dim=1):
    string = var_type
    if dim >= 1:
        string+=f' {name}[{str(dim)}];'
    elif dim <=0:
        string+=f' {name};'
    else:
        string+=f' {name};'
    
    return string

string = f'double state[{STATE_DIM}]'


print(add_variable('state', 'double', STATE_DIM))
print(add_variable('output', 'double', OUTPUT_DIM))
print(add_variable('input', 'double', INPUT_DIM))
print(add_variable('measurements', 'double', MEASUREMENTS_DIM))
print(args.mechanical)
print(args.planner)

# 
# TODO:
# ADD USER INPUTS
# ADD LOGGER AND USER INTERFACE  OPTIONS 
