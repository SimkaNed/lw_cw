from process_ticker import TickerProcess
from multiprocessing import Manager

# TODO:
# Maybe printer can be child of logger?


class Printer(TickerProcess):

    def __init__(self,
                 #  labels,
                 freq=60,
                 name='printer',
                 digits=4,
                 niceness=10):

        TickerProcess.__init__(self, freq, name=name, niceness=niceness)
        manager = Manager()
        self.output = manager.dict()
        self.digits = digits

    def set_labels(self, labels):
        self.labels = labels
        for label in self.labels:
            self.output[label] = 0
        self.label_size = len(self.labels)

    # def start(self):
    #     print('Printer have been started')
    #     super().start()

    def on_interrupt(self):
        print(self.label_size*'\n')

    def update_output(self, dict_to_print):
        # for label in self.labels:
        self.output.update(dict_to_print)

    def target(self):
        # print('The data\n', end=" ", flush=True)
        for label in self.labels:
            print(label,
                  round(self.output[label],
                        self.digits),
                  end="\n", flush=True)

        print((self.label_size)*'\033[A', end="\r", flush=True)
