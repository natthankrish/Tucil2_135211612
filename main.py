# import modules
from utils.divideAndConquer import *
from utils.visualization import *
from utils.generator import *
from utils.bruteforce import *

# import GUI
import tkinter
import tkinter.messagebox
import customtkinter
import time as t
import numpy as np
from PIL import ImageTk, Image

# setting customtkinter
customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("blue") 

class App(customtkinter.CTk):
    WIDTH = 1500
    HEIGHT = 750

    def __init__(self):
        super().__init__()
        #DEKLARASI VARIABEL
        self.title("Closest Pair of Point Using Divide and Conquer")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.dimension = None
        self.numOfPoints = None
        self.listPoint = []
        self.graph = None
        self.solution = None
        self.countEuclidean = None
        self.shortestDistance = None
        self.time = 0
        self.maxAxisVal = 10

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # Konfigurasi
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_right,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        # Frame 
        self.frame_right.columnconfigure(1, weight=6)
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.rowconfigure(0, weight=1)
        self.frame_right.rowconfigure(1, weight=2)
        self.frame_right.rowconfigure(2, weight=1)

        self.frame_input = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_input.grid(row=0, column=0, rowspan= 3, pady=20, padx=20, sticky="nsew")

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=1, rowspan= 3, pady=20, padx=20, sticky="nsew")

        # Frame Input
        self.frame_input.rowconfigure(0, weight=1)
        self.frame_input.rowconfigure(7, weight=7)
        self.frame_input.columnconfigure(0, weight=1)
        self.frame_input.columnconfigure(1, weight=1)
        self.headFrameInput = customtkinter.CTkLabel(master=self.frame_input,
                                                        text="Customize Your Data",
                                                        font=('Roboto Medium', -20))
        self.headFrameInput.grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="")

        self.dimension = customtkinter.CTkLabel(master=self.frame_input,
                                              text="Dimension of Point",
                                              font=("Roboto Medium", -16))  
        self.dimension.grid(row=1, column=0, pady=0, padx=10)

        self.dimensionBuffer = customtkinter.CTkEntry(master=self.frame_input,
                                                      placeholder_text="Integer (> 0)",
                                                      width=250)
        self.dimensionBuffer.grid(row=1, column=1, pady=5, sticky="w")


        self.numPointsLabel = customtkinter.CTkLabel(master=self.frame_input,
                                              text="Number of points",
                                              font=("Roboto Medium", -16))  
        self.numPointsLabel.grid(row=2, column=0, pady=0, padx=10)

        self.numPointsBuffer = customtkinter.CTkEntry(master=self.frame_input,
                                                      placeholder_text="Integer (> 1)",
                                                      width=250)
        self.numPointsBuffer.grid(row=2, column=1, pady=5, sticky="w")

        self.maxAxis = customtkinter.CTkLabel(master=self.frame_input,
                                              text="Axis Width",
                                              font=("Roboto Medium", -16))  
        self.maxAxis.grid(row=3, column=0, pady=0, padx=10)

        self.maxAxis = customtkinter.CTkOptionMenu(master=self.frame_input,
                                                        values=["10", "100", "1000"],
                                                        command=self.getMaxAxis)
        self.maxAxis.grid(row=3, column=1, pady=5, sticky="w")

        self.generateButton = customtkinter.CTkButton(master=self.frame_input,
                                                text="Generate",
                                                border_width=2, 
                                                width=120, 
                                                text_color="white",
                                                fg_color="#1f6aa5",  
                                                state="normal",
                                                command=self.checkvalid)
        self.generateButton.grid(row=4, column=0, columnspan=2, padx=20, pady=(20, 0))

        self.bufferValidityLabel = customtkinter.CTkLabel(master=self.frame_input,
                                              text="All points will be unique set of integers.",
                                              font=("Roboto Medium", -10))
        self.bufferValidityLabel.grid(row=5, column=0, columnspan=3, pady=0, padx=10, sticky="we")


        self.generatedPointLabel = customtkinter.CTkLabel(master=self.frame_input,
                                              text="Generated Points",
                                              font=("Roboto Medium", -16))
        self.generatedPointLabel.grid(row=6, column=0, columnspan=3, pady=0, padx=10)

        self.generatedPointFrame = customtkinter.CTkFrame(self.frame_input,
                                                          border_width=2, 
                                                          fg_color=("white", "gray38"))
        self.generatedPointFrame.grid(row=7, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")
        
        self.generatedPointCanvas = customtkinter.CTkCanvas(self.generatedPointFrame)

        self.generatedPointScrollbar = customtkinter.CTkScrollbar(self.generatedPointFrame, command=self.generatedPointCanvas.yview)
        self.generatedPointTextFrame = customtkinter.CTkFrame(self.generatedPointCanvas,
                                                              corner_radius=0, 
                                                              fg_color="white")
                                                            
        self.generatedPointCanvas.configure(yscrollcommand=self.generatedPointScrollbar.set, bg="white", highlightthickness=0)

        self.generatedPointTextLabel = customtkinter.CTkLabel(master=self.generatedPointTextFrame,
                                                              text="",
                                                              font=("Roboto Medium", -12), 
                                                              fg_color="white",
                                                              justify="left",
                                                              anchor="w",
                                                              text_color="gray38")
        
        
        self.generatedPointTextLabel.pack(fill="both", expand=True)

        self.generatedPointCanvas.bind(
            "<Configure>",
            lambda e: self.generatedPointCanvas.configure(
                scrollregion=self.generatedPointCanvas.bbox("all")
            )
        )
        self.generatedPointCanvas.configure(height=self.generatedPointTextLabel.winfo_height())

        self.generatedPointCanvas.create_window((0, 0), window=self.generatedPointTextFrame, anchor="nw")
        self.generatedPointCanvas.pack(side="left", fill="both", expand=True)
        self.generatedPointScrollbar.pack(side="right", fill="y")

        # Layout Gambar
        self.frame_info.rowconfigure(0, weight=0)
        self.frame_info.rowconfigure(1, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.frame_info.configure(height=self.frame_input.winfo_height())

        self.graphLabel = customtkinter.CTkLabel(master=self.frame_info,
                                              text="Graph Plot",
                                              font=("Roboto Medium", -28))  
        self.graphLabel.grid(row=0, column=0, padx=20, pady=20)


        self.solutionLabel = customtkinter.CTkLabel(master=self.frame_info,
                                                   corner_radius=6,
                                                   text = "",
                                                   font=("Roboto Medium", -28),
                                                   fg_color=("white", "gray38"),
                                                   justify=tkinter.LEFT)
        self.solutionLabel.grid(column=0, row=1, sticky="nsew", pady=15)

        self.label_infot3 = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Execution time: ",
                                              font=("Roboto Medium", -15),
                                              justify = "left")  
        self.label_infot3.grid(row=3, column=1, columnspan=2, sticky="nw")

        # set default values
        self.optionmenu_1.set("Dark")
        
    def getMaxAxis(self, newMaxAxis):
        self.maxAxisVal = int(newMaxAxis)
    
    def getVisualization(self):
        if self.dimension <= 3:
            getGraph(self.dimension, self.numOfPoints, self.listPoint, self.solution, self.maxAxisVal)
            self.graph = ImageTk.PhotoImage(Image.open("bin/currentPlot.png").resize((int(self.solutionLabel.winfo_height()*1.3), self.solutionLabel.winfo_height()), Image.ANTIALIAS), master=self.solutionLabel)
            self.solutionLabel.configure(image=self.graph)
            self.solutionLabel.configure(text="")
        else:
            self.solutionLabel.configure(image="")
            self.solutionLabel.configure(text="Not Available For Dimension > 3")
        distanceBrute, solutionBrute, countBrute = bruteForce(self.numOfPoints, self.listPoint)
        generateTerminal(distanceBrute, countBrute, solutionBrute, self.solution, self.countEuclidean, self.shortestDistance, self.listPoint)

    def displayPoints(self, textToDisplay):
        self.generatedPointCanvas.destroy()
        self.generatedPointTextFrame.destroy()
        self.generatedPointTextLabel.destroy()
        self.generatedPointScrollbar.destroy()

        self.generatedPointCanvas = customtkinter.CTkCanvas(self.generatedPointFrame)
        self.generatedPointScrollbar = customtkinter.CTkScrollbar(self.generatedPointFrame, command=self.generatedPointCanvas.yview)
        self.generatedPointTextFrame = customtkinter.CTkFrame(self.generatedPointCanvas,
                                                              corner_radius=0, 
                                                              fg_color="white")
                                                            
        self.generatedPointCanvas.configure(yscrollcommand=self.generatedPointScrollbar.set, bg="white", highlightthickness=0)

        self.generatedPointTextLabel = customtkinter.CTkLabel(master=self.generatedPointTextFrame,
                                                              text=textToDisplay,
                                                              font=("Roboto Medium", -12), 
                                                              fg_color="white",
                                                              justify="left",
                                                              anchor="w",
                                                              text_color="gray38",
                                                              height=self.generatedPointCanvas.winfo_height())
        
        self.generatedPointTextLabel.grid(row=0, column=0, padx=20, pady=20)
        self.generatedPointCanvas.configure(height=self.generatedPointTextLabel.winfo_height())
        self.generatedPointCanvas.bind(
            "<Configure>",
            lambda e: self.generatedPointCanvas.configure(
                scrollregion=self.generatedPointCanvas.bbox("all")
            )
        )
        self.generatedPointCanvas.create_window((0, 0), window=self.generatedPointTextFrame, anchor="nw")
        self.generatedPointCanvas.pack(side="left", fill="both", expand=True)
        self.generatedPointScrollbar.pack(side="right", fill="y")

    def process(self):
        begin = t.perf_counter()
        self.listPoint = pointGenerator(self.dimension, self.numOfPoints, self.maxAxisVal)
        listOfAllPoints = stringDisplayGenerator(self.listPoint, self.numOfPoints, self.dimension)
        self.displayPoints(listOfAllPoints)
        self.shortestDistance, self.solution, self.countEuclidean = shortestDistance(self.dimension, self.numOfPoints, self.listPoint)
        self.getVisualization()
        end = t.perf_counter()
        self.time = end-begin
        self.label_infot3.configure(text=stringOutputGenerator(self.time, self.solution, self.dimension, self.shortestDistance, self.countEuclidean))

    def checkvalid(self):
        self.dimension = self.dimensionBuffer.get()
        self.numOfPoints = self.numPointsBuffer.get()
        self.listPoint = []
        if (self.dimension.isnumeric() and self.numOfPoints.isnumeric()):
            self.dimension = int(self.dimension)
            self.numOfPoints = int(self.numOfPoints)
            if (not self.dimension > 0 or not self.numOfPoints > 1):
                self.bufferValidityLabel.configure(text="Dimension should be integer > 0 and Number of points should be integer > 1")
            else:
                if (self.numOfPoints > ((2*self.maxAxisVal + 1) ** self.dimension)):
                    self.bufferValidityLabel.configure(text="Number of points should be lower than (2 *Axis Width)^dimension + 1")
                else:
                    self.process()
        else:
            if self.dimension.isnumeric() and not self.numOfPoints.isnumeric():
                self.bufferValidityLabel.configure(text="Number of points should be integer > 1")
            elif not self.dimension.isnumeric() and self.numOfPoints.isnumeric():
                if (int(self.numOfPoints) > 0):
                    self.bufferValidityLabel.configure(text="Dimension should be integer > 0")
                else:
                    self.bufferValidityLabel.configure(text="Dimension should be integer > 0 and Number of points should be integer > 1")
            else:
                self.bufferValidityLabel.configure(text="Dimension should be integer > 0 and Number of points should be integer > 1")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.quit()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
