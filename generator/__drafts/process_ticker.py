from multiprocessing import Process, Array, Value, Manager
from time import perf_counter
from os import nice


# TODO:
# set the process priority
# get the process ID

class TickerProcess:
    def __init__(self,
                 freq=100,
                 name='ticker',
                 #  args = None
                 niceness=5,
                 ):

        self.process = Process(target=self.ticker_process)

        # self.target = target
        # self.name = f'{name} {}'
        self.name = name
        self.freq = freq
        self.time = 0
        self.niceness = niceness
        self._shared = Manager().Namespace()
        self._shared.is_active = False

        # get the process id

    def __del__(self):
        print(f'{self.name} was deleted from memory')

    def on_init(self):
        pass

    def on_while(self):
        pass

    def target(self):
        pass

    def on_interrupt(self):
        pass

    def _set_priority(self):
        old_nice_value = nice(0)
        increment = self.niceness - old_nice_value
        niceness = nice(increment)
        # print(f'\n{self.name} process niceness is {niceness}')

    def start(self):
        self._shared.is_active = True
        self.process.start()

    def close(self):
        self.process.join(timeout=0.)
        self.process.terminate()

    def pause(self):
        self._shared.is_active = False
        # print('Is in pause')

    def resume(self):
        # print('resumed')
        self._shared.is_active = True

    def ticker_process(self):
        self._set_priority()
        # print()
        init_time = perf_counter()
        ticker_time = 0
        self.on_init()
        try:
            while True:
                if self._shared.is_active:
                    self.time = perf_counter() - init_time
                    self.on_while()
                    if (self.time - ticker_time) >= 1/self.freq:
                        self.target()
                        ticker_time = self.time

        except KeyboardInterrupt:
            self.on_interrupt()
            print(f'\n{self.name} process is over due KeyboardInterrupt...')

        except Exception as e:
            raise Exception(e.message)
