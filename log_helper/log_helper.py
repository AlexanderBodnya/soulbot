import logging
import logging.handlers



class LogHelper(logging.Logger):
    
    levels = {
        0 : logging.CRITICAL,
        1 : logging.ERROR,
        2 : logging.WARNING,
        3 : logging.INFO,
        4 : logging.DEBUG
        }
    # Redefining logging levels for convinience purposes 

    def __init__(self,log_level,logger_name):
        logging.getLogger(logger_name)
        logging.basicConfig(
            format='%(processName)s %(process)d %(levelname)s %(asctime)s %(message)s', 
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=self.levels[log_level]
            )
    # Instance initialization function takes logger name as argument and provides instance of logger with defined format parameters
    
    def log_message(self, level, *args):
        logging.log(self.levels[level], *args)
    # Redefined logging.log function, which allows to take logging levels as int numbers    

        
         
        
        
        
log = LogHelper(4,'test_log')
log.log_message(4, '%s before you %s', 'Look', 'leap!')
