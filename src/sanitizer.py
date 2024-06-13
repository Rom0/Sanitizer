import re
# import logger
from datetime import datetime

class Logger:
    file_path = ""

    def log(msg):
        with open(Logger.file_path, "w") as file:
            file.write(f"{datetime.now()} - {msg}")
        file.close()

    def log_start(obj, **args):
        string = f"Began process {obj.getSpotterUID()} on file blank\n"
        Logger.log(string)

    def log_removal(obj, data):
        #DATETIME SPOTTERUID REMOVED THIS STRING: ------
        string = f"Spotter {obj.getSpotterUID()} removed {data}\n"
        Logger.log(string)
    
    def log_end(obj, num):
        string = f"Spotter {obj.getSpotterUID()} ended process with {num} removals.\n"
        Logger.log(string)

    def log_error(obj, error, msg):
        string = f"{error} - Spotter {obj.getSpotterUID()}: {msg} \n"
        Logger.log(string)
        
        

class Spotter:
    
    regex = {"SIN":"",
             "email": "",
             "phone": "",
             "address": ""}
    
    def __init__(self, options: list[str] =[] ):
        self.options = options
        self.curr_spotter:str = ""
        self.enabled_regex:dict[str, str] = {}
        self.setup()


    def setup(self):
        if not self.options:
            self.enabled_regex = Spotter.regex
        else:
            
            option:str
            for option in self.options:
                if option not in self.enabled_regex:
                    self.enabled_regex[option] = Spotter.regex[option]
        

    def getSpotterUID(self):
        return self.curr_spotter
    
    def process(self, text: str):
        for spotter, expr in self.enabled_regex.items():
            Logger.log_start(self)
            removal_count = 0
            self.curr_spotter = spotter
            try:
                text_segment = ""
                #run text
                #log each removal
                Logger.log_removal(self, text_segment)
                pass
            except Exception as e:
                #log error
                Logger.log_error(self, e, e.args)
                pass
            # log count of each regex removal 
            Logger.log_end(self, removal_count)

        

class SINSpotter(Spotter):

    def process(self, text:str):
        pass