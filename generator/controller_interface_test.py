

# control unit interface with LCM
#
# ////////////////
# ///// LCM //////
# ////////////////
#
# CONTROLLER_STATE (PUBLISH)
#     int64_t  timestamp;
#     double   state[STATE_DIM];
#     double   state_estimates[STATE_DIM];
#     double   output[OUTPUT_DIM];
#     double   input[INPUT_DIM];
#     string   plant_name;
#     bool     active;
#
# USER_COMMANDS (PARSE)
#     int64_t timestamp;
#     int16_t  mode;
#     double   measurements[MEAS_DIM];
#     int32_t error_code;
#     // The commands to add

# PLANT_STATE (PARSE)
# const int16_t STATE_DIM=2, OUTPUT_DIM = 1, INPUT_DIM=1;
# int64_t timestamp;
# int16_t  mode;
# double   measurements[MEAS_DIM];
# int32_t error_code;
# // The commands to add

# //////////////////////
# /// SHARED MEMORY ////
# //////////////////////
#
#  CONTROL_UNIT STATES
#    - desired_state
#    - reference_state  (if planner)
#    - reference_control (if planner)
#    - estimated_states
#    - control
#    - output
#

import lcm
from time import perf_counter
from system.protocol import user_commands_t, controller_states_t, plant_states_t
from multiprocessing import Process, Manager
from system.parameters import STATE_DIM, OUTPUT_DIM, INPUT_DIM, MEASUREMENTS_DIM, USER_INPUT_DIM


# TODO:
#  - add address
#  - store shared states not in Namespace but Arrays

class ControlUnit:
    def __init__(self, address=None) -> None:

        # INITIALIZE SHARED MEMORY 
        self.control_unit = Manager().Namespace()

        self.control_unit.desired_state = 0
        self.control_unit.reference_state = 0
        self.control_unit.reference_control = 0
        self.control_unit.estimated_states = 0
        self.control_unit.control = 0
        self.control_unit.output = 0

        self.user_commands = Manager().Namespace()
        self.user_commands.desired_postion = 0
        

        # /////// SETLING LCM ///////

        self.address = address
        # Initialize LCM
        self.lcm_node = lcm.LCM(self.address)
        # Define channels
        self.user_channel = "user"
        self.controller_channel = "controller"
        self.plant_channel = "plant"
        # Initiate the messages
        self.controller_message = controller_states_t()
        self.plant_message = plant_states_t()
        self.user_message = user_commands_t()

        # self.subscriptions = []

        # self.command_message = command_t()

    # def sta

    def update_user_command(self, channel, data):
        pass

    def update_plant(self, channel, data):
        pass

    def update_output(self, channel, data):
        pass

    def subscribe(self):
        """Subscribe to plant and user commands"""
        self.plant_subscription = self.subscribe(self.plant_channel, self.update_plant)
        self.user_subscription = self.subscribe(self.user_channel, self.update_user_command)
    
    def publish(self):
        """publish the controller states to LCM"""
        self.controller_message.state_estimates = self.control_unit.estimated_states
        self.controller_message.output = self.control_unit.output
        self.controller_message.input = self.control_unit.control

        self.lc.publish(self.controller_channel, self.controller_message.encode())
           
    def handle_lcm(self):
        """Handle LCM subscriptions"""
        self.lc.handle()
        # pass

    def set_states(self):
        pass

    def set_control(self):
        pass

    def get_user_command(self):
        pass

    def get_plant_state(self):
        pass

    def set_control(self):
        pass

    # handle()

# commands = Manager().Namespace()


# # address = "udpm://239.255.76.67:7667?ttl=1"

# states = Manager().Namespace()
# commands = Manager().Namespace()

# def state_callback(channel, data):
#     state_data = state_t.decode(data)
#     states.name = state_data.name
#     states.time = state_data.timestamp
#     states.state = state_data.state
#     states.state_estimates = state_data.state_estimates
#     states.output = state_data.output
#     states.input = state_data.input
#     states.error_flags = state_data.error_flags
#     states.active = state_data.active

# ZERO_INPUT = command_t().input


# class LCMControllerInterface(lcm.LCM):

#     def __init__(self, address = "") -> None:
#         lcm.LCM.__init__(self, address)

#         self.state_channel = "states"
#         self.command_channel = "commands"

#         self.subscription = self.subscribe(self.state_channel, state_callback)
#         self.command_message = command_t()

#     def __del__(self) -> None:
#         self.send_control()
#         self.unsubscribe(self.subscription)
#         lcm.LCM.__del__(self)
#         print('Unsubscribed')


#     def update_state(self) -> None:
#         self.handle()

#     def send_control(self, control=ZERO_INPUT) -> None:
#         self.command_message.input = control
#         self.publish(self.command_channel, self.command_message.encode())

#     def send_commands(self, commands) -> None:
#         pass


# class LCMControllerProcess():

#     def __init__(self, address = "", update_rate = None) -> None:

#         self.address = address
#         self._process = Process(target=self.lcm_process)
#         self._shared = Manager().Namespace()
#         self._shared.is_active = False

#     def __del__(self) -> None:
#         print('deleted')

#     def lcm_process(self):
#         self.lcm = LCMControllerInterface(address =  self.address)
#         self._shared.is_active = True
#         while True:
#             if self._shared.is_active:
#                 self.lcm.send_control()
#                 self.lcm.update_state()

#     def start(self):
#         self._process.start()
#         print('started')

#     def pause(self):
#         self._shared.is_active = False
#         print('Is in pause')

#     def resume(self):
#         print('resumed')
#         self._shared.is_active = True


#     def stop(self):
#         self._process.terminate()

#     def update_states(self):
#         pass

#     def update_command(self):
#         pass

# №4-258-36246.
