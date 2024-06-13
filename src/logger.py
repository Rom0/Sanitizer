
class Logger:

    def __init__(self, file_path:str, verbose: bool = False) -> None: 
        self.verbose:bool = verbose
        self.file_path = file_path
        
    def log(self, text):
        
        with open(self.file_path) as file:
            file.write(text)

        file.close()