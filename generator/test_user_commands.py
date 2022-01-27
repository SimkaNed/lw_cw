import lcm
from system.protocol import user_commands_t
from system.parameters import USER_CHANNEL
from time import perf_counter, sleep


lcm_node = lcm.LCM()

user_message = user_commands_t()

try:
    print('The set point parser is started...\n\n')
    initial_time = perf_counter()
    while True:
        # user_input_1 = float(input('Print the input: '))
        time = perf_counter() - initial_time
        user_message.timestamp = int(time*1000)
        lcm_node.publish(USER_CHANNEL, user_message.encode())
        sleep(0.01)
        # print(user_message.timestamp)
except KeyboardInterrupt:
    # command_message.position = 0
    # command_message.speed = 0
    # user_message.timestamp = 0 
    lcm_node.publish(USER_CHANNEL, user_message.encode())
    print('The user interface is over...\n\n')




