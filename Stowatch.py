import time 
import cv2 as cv 
import numpy as np


class Display (): 
    
    def __init__ ( self, size, color ): 
        self.background = np.zeros( size ) 
        self.center = ( int( size[0] / 2 - 130 ),   int( size[1] / 2 - 100 ) )    
        self.color = color  
        self.size = size
    
    def clear_background ( self ) : 
        self.background = np.zeros( self.size )

class Stopwatch: 
    
    def __init__ ( self, display, start_point ):
        self.start_point = start_point 
        self.display = display
        
    def struct_time ( self ): 
        now_point = time.time() - self.start_point
        
        minutes = str ( int ( now_point / 60 ) ) 
        seconds = str ( int ( now_point % 60 ) )
        
        if len (  minutes )  == 1: 
            minutes = "0" + minutes
        
        if len ( seconds ) == 1: 
            seconds = "0" + seconds
            
        return str("{:} : {:}".format( minutes, seconds ) )
    
    def show_time  ( self ): 
        
        self.display.clear_background()
    
        cv.putText(
                    self.display.background, #numpy array on which text is written
                    self.struct_time(), #text
                    self.display.center, 
                    cv.FONT_HERSHEY_SIMPLEX, #font family
                    5, #font size
                    self.display.color , #font color
                    6) #font stroke
    
        cv.imshow("Cronômetro", self.display.background)
        key = cv.waitKey(1)
        
        if key != -1:
            key_pressed (key)
    
def key_pressed ( key ):
    
    if key == 113: 
        quit() 
    
    if key == 122: 
        stopwatch.start_point = time.time()
        
        
stopwatch = Stopwatch ( Display( size = ( 720, 1080, 3) , color =  (255, 0, 0) ), time.time() )

while (True): 
    stopwatch.show_time()