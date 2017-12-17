import threading
import time

class my_thread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    pkts=[] 

    def __init__(self):
        super(my_thread, self).__init__()
        self._stop_event = threading.Event()
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()  

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    def run(self):
        """ Method that runs forever """
        while not self.stopped():
            # Do something
            print('Doing something imporant in the background')

    def return_packets(): # this function is to retrive the packets outside the thread
        return my_thread.pkts


t = my_thread()
time.sleep(1)
t.stop()