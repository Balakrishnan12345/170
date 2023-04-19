from tkinter import *

root=Tk()
root.title("170")
root.geometry("900x900")
root.config(bg="lightblue")

class History_in_space():
    def year_2008(self):
        print("/n","Achievements occurred in year 2008","/n")

        print("India successfully launched Chandrayaan in 2008 in order to explore the moon.The craft was inserted into lunar orbit in its first attempt. One of the greatest achievement of Chandrayaan was the discovery of the water molecules in the lunar soil.")

    def year_2011(self):
        print("/n","Achievements occurred in year 2008","/n")
        
class History_in_Medial():
    def year_2008(self):
        print("/n","Achievements occurred in year 2008","/n")
        print("Although scientists have long discovered how malaria is transferred and know how to prevent it, nearly 1 million people die every year from the disease, according to international estimates.Finally, Dec. 8, the first results of a malaria vaccine that shows promise hit international news.")
        
    def year_2011(self):
        print("/n","Achievements occurred in year 2008","/n")
        
class History_in_Sports():
    def year_2008(self):
        print("/n","Achievements occurred in year 2008","/n")
        print("In 2008, Abhinav Bindra created history by bagging gold in men's 10m air rifle event at the Beijing Games. His gold remains the country's first and only individual gold medal till date.")
        
    def year_2011(self):
        print("/n","Achievements occurred in year 2011","/n")
        print("/n","Achievements occurred in year 2008","/n")
        
        
space = History_in_space()
space.year_2008()
space.year_2011()

Medial = History_in_Medial()
Medial.year_2008()
Medial.year_2011()


Sports = History_in_Sports()
Sports.year_2008()
Sports.year_2011()

root.mainloop()


 
