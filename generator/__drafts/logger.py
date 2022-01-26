from .process_builder import TickerProcess
from multiprocessing import Manager
from numpy import savetxt, array

class Logger(TickerProcess):
    
    def __init__(self,
                 freq=100,
                 name='logger',
                 file_path = 'log.csv',
                 niceness = 10
                 ):

        
        TickerProcess.__init__(self, freq, name=name, niceness = niceness)
        manager = Manager()
        self.file_path = file_path
        self.input_dict = manager.dict()
        self.output_dict = manager.dict()
        


    def set_labels(self, labels):
        self.labels = labels
        for label in self.labels:
            self.input_dict[label] = 0
            self.output_dict[label] = []


    def log_data(self, dict_to_log):
        for label in self.labels:
            self.input_dict[label] = dict_to_log[label]


    def on_init(self):

        self.storage = {}
        for label in self.labels:
            self.storage[label] = []


    def save_file(self, file_path=None):
        output = []
        if not file_path:
            file_path = self.file_path

        for label in self.labels:
            output.append(self.output_dict[label])
        
        print(output[0])
        # print()
        output_array = array(output).T
        # output_array = output_array[:-2]
        savetxt(file_path, output_array, delimiter=',')


    def get_storage(self):
        return self.output_dict


    def target(self):
        for label in self.labels:
            self.storage[label].append(self.input_dict[label])             
            self.output_dict[label] = self.storage[label] 


