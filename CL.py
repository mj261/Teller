#the thread that runs the user input/output
class commandLine(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.counter = 0
		
		
	#list functions that can ben executed here
	
	#end functions
      
    def run(self):
        input = ""		
        
		#match input to function list and call appropriate functions

			
			
			