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
        if self.miliSec > 1000:
            self.miliSec -= 1000 
            self.sec += 1 
        if self.sec > 60:
            self.sec -= 60
            self.min += 1 
        if self.min > 60:
            self.min -= 60 
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
        
        self.resetButton = Button(self,text="reset",width=10,height=2,command=self.restart)
        self.resetButton.grid(row=1,column=0)
        
        self.changeStateButton = Button(self,text="stop",width=10,height=2,command=self.stop)
        self.changeStateButton.grid(row=2,column=0)

        self.increment()
    
    def increment(self):
        self.counterLabel["text"] = str(self.counter)
        if self.startTime:    
            self.counter.add()
        self.after(1,self.increment)

    def restart(self):
        self.counter.restart()
        self.counterLabel["text"] = str(self.counter)
    
    def stop(self):
        if self.startTime:
            self.startTime = False 
            self.changeStateButton["text"] = "start"
        else: 
            self.startTime = True 
            self.changeStateButton["text"] = "stop"

root = Tk()
timeKeeper = counterFrame(root)
root.mainloop()
