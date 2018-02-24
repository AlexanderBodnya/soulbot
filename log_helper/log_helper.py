import logging
import logging.handlers
import time



class LogHelper(logging.Logger):
    
    levels = {
        0 : logging.CRITICAL,
        1 : logging.ERROR,
        2 : logging.WARNING,
        3 : logging.INFO,
        4 : logging.DEBUG
        }
    # Redefining logging levels for convinience purposes 

    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        
        self.formatter = logging.Formatter('%(processName)s %(process)d %(levelname)s %(asctime)s %(message)s', 
            datefmt='%m/%d/%Y %I:%M:%S %p'
            )
    # Instance initialization function takes logger name as argument and provides instance of logger with defined format parameters
    
    def log_message(self, level, *args):
        self.logger.log(self.levels[level], *args)
        
    # Redefined logging.log function, which allows to take logging levels as int numbers    

    def set_level(self,log_level):
        self.logger.setLevel(self.levels[log_level])
        
    # Set log level of the logger instance
        
    def file_handler(self):
        filename = time.strftime("%Y%m%d-%H%M%S")+'_soulbot.log'
        handler = logging.FileHandler(filename)
        handler.setFormatter(self.formatter)
        return handler
    
    # Create handler to send logs to the file
    
    def stream_handler(self):
        handler = logging.StreamHandler()
        handler.setFormatter(self.formatter)
        return handler
    
    # Create handler to send logs to the stdout
        
    def attach_handler(self, handler):
        self.logger.addHandler(handler)
        
    # Attach handler tot the logger instance



#some examples       
        
log = LogHelper('test_log')
log.set_level(3)
sh = log.stream_handler()
log.attach_handler(sh)
log.log_message(3, '%s before you %s', 'Look', 'leap!')
handler = log.file_handler()
log.attach_handler(handler)
log.log_message(0, '%s before you %s', 'Look', 'leap!')
log.log_message(3, '%s before you %s', 'Look', 'leap!')
log.log_message(4, '%s before you %s', 'Look', 'leap!')