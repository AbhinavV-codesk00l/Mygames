from tkinter import *
class timer:
    """
    represents the time in the form hour:min:sec:milisecend
    """
    def __init__(self):
        """
        __init__(self) -> timer 
        this keeps track of what the time is in a time string
        """
        self.hour = 0 
        self.min = 0 
        self.sec = 0
        self.miliSec = 0 

    def __str__(self):
        """
        str(self) -> str
        returns the time in a string
        """
        return f"{self.hour}:{self.min}:{self.sec}:{self.miliSec}"

    def add(self):
        """
        add() 
        adds one millisecond to the timer
        """
        self.miliSec += 1 
        if self.miliSec > 999:
            self.miliSec -= 999 
            self.sec += 1 
        if self.sec > 59:
            self.sec -= 59
            self.min += 1 
        if self.min > 59:
            self.min -= 59 
            self.hour += 1 

    def restart(self):
        self.hour,self.min,self.sec,self.miliSec = 0,0,0,0 

class counterFrame(Frame):
    """
    frame for the counter app
    """
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.counter = timer()
        self.startTime = True 
        
        self.counterLabel = Label(self,width=35,height=5,relief=RAISED,text=str(self.counter))
        self.counterLabel.grid(row=0,column=0)
        
        self.resetButton = Button(self,text="reset",width=10,height=2,command=self.counter.restart)
        self.resetButton.grid(row=1,column=0)

        self.stopButton = Button(self,text="stop",width=10,height=2,command=self.changeState)
        self.stopButton.grid()
        
        self.increment()
    
    def increment(self):
        self.counterLabel["text"] = str(self.counter)
        if self.startTime:    
            self.counter.add()
            self.after(1,self.increment)
    
    def changeState(self):
        self.counterLabel["text"] = str(self.counter)
        if self.startTime:
            self.startTime = False 
            self.stopButton["text"] = "start"
        else:
            self.startTime = True 
            self.stopButton["text"] = "stop"
