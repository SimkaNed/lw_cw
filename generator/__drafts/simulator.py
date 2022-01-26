# from multiprocessing.sharedctypes import Value
from .process_builder import TickerProcess
from multiprocessing import Manager
from numpy import savetxt, array



class Simulator(TickerProcess):
    
    def __init__(self,
                 f=None,  # The function to integrate
                 n = 2, # State dimensions
                 m = 1, # Control dimensions
                 x0 = None,
                 sim_type='real',  # type of simulation
                 dt=5e-4,
                 scale=10):
        

#         TickerProcess.__init__(self, freq, name=name)
#         manager = Manager()

#         # self.file_path = file_path
#         # self.input_dict = manager.dict()
#         # self.output_dict = manager.dict()


#     def set_labels(self, labels):
#         self.labels = labels
#         for label in self.labels:
#             self.input_dict[label] = 0
#             self.output_dict[label] = []


#     def log_data(self, dict_to_log):
#         for label in self.labels:
#             self.input_dict[label] = dict_to_log[label]


#     def on_init(self):
#         self.storage = {}
#         for label in self.labels:
#             self.storage[label] = []


#     def save_file(self, file_path=None):
#         if not file_path:
#             file_path = self.file_path

#         for label in self.data_labels:
#             self.output.append(self.output_dict[label])
        
#         output = array(self.output).T
#         savetxt(file_path, output, delimiter=',')


#     def get_storage(self):
#         return self.output_dict


#     def target(self):
#         for label in self.labels:
#             self.storage[label].append(self.input_dict[label])             
#             self.output_dict[label] = self.storage[label] 


