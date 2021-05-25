from tkinter import *
from tkinter import messagebox
import time
import threading

class Neuron():

    def __init__(self, synapses, isActive, coordX, coordY):

        self.synapses = synapses
        self.isActive = isActive
        self.imageActive = PhotoImage(file='activeNeuronSmall.png')
        self.imageNotActive = imageNotActive = PhotoImage(file = 'inactiveNeuronSmall.png')
        self.coordX = coordX
        self.coordY = coordY
        pass

    def _toggleActivation(self):

        if(self.isActive == True):
            self.isActive = False
            self.button['image'] = self.imageNotActive
        else:
            self.isActive = True
            self.button['image'] = self.imageActive
        pass


    def _createButton(self, board):

        if(self.isActive == True):
            self.button = Button(board.root, image = self.imageActive, command = self._toggleActivation, borderwidth = 0)
        else:
            self.button = Button(board.root, image = self.imageNotActive, command = self._toggleActivation, borderwidth = 0)

        self.button.place(x = self.coordX, y = self.coordY)
        pass

    def _drawSynapses(self, board):
        for i in self.synapses:
            board.canvas.create_line(self.coordX+8, self.coordY+8, i[0]+8, i[1]+8, fill = 'red')

        pass



class Board():
    root = 0

    def __init__(self, w, h):
        self.root = Tk()
        self.root.geometry(str(w) + 'x' + str(h))
        self.canvas = Canvas(self.root, width = w, height = h)
        self.canvas.pack()
        pass

mainBoard = Board(700, 700)


outputNeurons = [0] * 7

hiddenLayer1 = [0] * 35
hiddenLayer1Synapses = [[0,0]]* len(outputNeurons)

inputNeurons = [0] * 63
inputNeuronsSynpses = [[0,0]]* len(hiddenLayer1)

for i in range(0, 7):
    outputNeurons[i] = Neuron(False, False, 330, 18+ 20*i)
    outputNeurons[i]._createButton(mainBoard)
    hiddenLayer1Synapses[i] = [330, 18+ 20*i]

for i in range(0, 35):
    hiddenLayer1[i] = Neuron(hiddenLayer1Synapses, True, 170, 10+ 20*i)
    hiddenLayer1[i]._createButton(mainBoard)
    hiddenLayer1[i]._drawSynapses(mainBoard)
    inputNeuronsSynpses[i] = [170, 10+ 20*i]

for i in range(0, 63):
    inputNeurons[i] = Neuron(inputNeuronsSynpses, False, 10, 10+ 20*i)
    inputNeurons[i]._createButton(mainBoard)
    inputNeurons[i]._drawSynapses(mainBoard)


mainloop()