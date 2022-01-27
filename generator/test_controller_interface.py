import lcm
from time import perf_counter, sleep
from multiprocessing import Process, Manager
from system.protocol import user_commands_t, controller_states_t, plant_states_t
from system.parameters import STATE_DIM, OUTPUT_DIM, MEASUREMENTS_DIM, USER_INPUTS_DIM, CONTROL_DIM, CONTROLLER_CHANEL, USER_CHANNEL, PLANT_CHANNEL
from numpy import zeros

# TODO:
#  - add address chooser with default values 
#  - store shared states not in Namespace but Arrays
#  - move shared variables from control unit class

# NOTE:
#  - the example of UDP multicast address:
#    lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

class ControlUnit:
    def __init__(self,
                 address='',
                 verbose=False) -> None:
        
        self.verbose = verbose
        
        # INITIALIZE SHARED MEMORY
        # CONTROLLER
        self.control_unit = Manager().Namespace()
        self.timestamp = 0
        self.control_unit.desired_state = zeros(STATE_DIM)
        self.control_unit.estimated_states = zeros(STATE_DIM)
        self.control_unit.reference_state = zeros(STATE_DIM)
        self.control_unit.control = zeros(CONTROL_DIM)
        self.control_unit.reference_control = zeros(CONTROL_DIM)
        self.control_unit.plant_output = zeros(OUTPUT_DIM)

        # USER
        self.user_commands = Manager().Namespace()
        self.user_commands.timestamp = 0
        self.user_commands.desired_state = zeros(STATE_DIM)
        self.user_commands.user_inputs = zeros(USER_INPUTS_DIM)
        self.user_commands.desired_outputs = zeros(OUTPUT_DIM)
        # self.user_commands.us

        # PLANT
        self.plant = Manager().Namespace()
        self.plant.timestamp = 0
        self.plant.measurements = zeros(MEASUREMENTS_DIM)
        self.plant.plant_output = zeros(OUTPUT_DIM)

        # /////// SETLING LCM ///////

        self.address = address
        # Initialize LCM
        self.lcm_node = lcm.LCM(self.address)

        # Define channels
        self.user_channel = USER_CHANNEL
        self.controller_channel = CONTROLLER_CHANEL
        self.plant_channel = PLANT_CHANNEL

        # Initiate the messages
        self.controller_message = controller_states_t()
        self.plant_message = plant_states_t()
        self.user_message = user_commands_t()

        # self.subscribe()

    def __del__(self):
        pass
        # self.unsubscribe()
    # ///////////////////////////////
    # USER AND PLANT MESSAGES PARSERS
    # ///////////////////////////////

    def update_user_command(self, channel, data):
        """Get user data from LCM and store to shared variables"""
        user_data = user_commands_t.decode(data)
        self.user_commands.timestamp = user_data.timestamp
        self.user_commands.desired_state = user_data.desired_state
        self.user_commands.user_inputs = user_data.user_inputs
        self.user_commands.desired_outputs = user_data.desired_outputs

    def update_plant(self, channel, data):
        """Get plant data from LCM and store to shared variables"""
        plant_data = plant_states_t.decode(data)
        self.plant.timestamp = plant_data.timestamp
        self.plant.measurements = plant_data.measurements
        self.plant.plant_output = plant_data.plant_output

        # if self.ver

    def subscribe(self):
        """Subscribe to plant and user commands"""

        self.plant_subscription = self.lcm_node.subscribe(self.plant_channel,
                                                          self.update_plant)

        self.user_subscription = self.lcm_node.subscribe(self.user_channel,
                                                   self.update_user_command)
        
        if self.verbose:
            print(f'subscribed to {self.user_channel} and {self.plant_channel} channels')

    def unsubscribe(self):
        """Unsubscribe from plant and user commands"""
        self.lcm_node.unsubscribe(self.plant_subscription)
        self.lcm_node.unsubscribe(self.user_subscription)

        if self.verbose:
            print(f'unsubscribed from {self.user_channel} and {self.plant_channel} channels')


    def publish(self):
        """Publish the controller states to LCM"""
        
        self.controller_message.desired_state = self.control_unit.desired_state 
        self.controller_message.estimated_states = self.control_unit.estimated_states 
        self.controller_message.reference_state = self.control_unit.reference_state 
        self.controller_message.control = self.control_unit.control 
        self.controller_message.reference_control = self.control_unit.reference_control
        self.controller_message.plant_output = self.control_unit.plant_output 

        self.lcm_node.publish(self.controller_channel,
                              self.controller_message.encode())

    def handle_lcm(self):
        """Handle LCM subscriptions"""
        self.lcm_node.handle()



controller_interface = ControlUnit(verbose=True)
controller_interface.subscribe()
 
try:
    while True:
        print(controller_interface.user_commands)
        controller_interface.handle_lcm()

except KeyboardInterrupt:
    controller_interface.unsubscribe()