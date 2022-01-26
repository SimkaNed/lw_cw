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

