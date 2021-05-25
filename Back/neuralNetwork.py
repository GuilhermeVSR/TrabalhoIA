import numpy as np

class MLP:
    
    def __init__(self, nInputs, nHidden, nOutputs):
        self.nInputs = nInputs
        self.nHidden = nHidden
        self.nOutputs = nOutputs

        layers = [self.nInputs] + [self.nHidden] + [self.nOutputs]

        print(layers)


        #create random wheight matrix
        self.weights = []
        for i in range(0, len(layers) - 1):
            self.weights.append(np.random.rand(layers[i], layers[i+1]))

        print(self.weights)

    def ForwardPropagate(self, inputs):
        activations = inputs

        for i in self.weights:
            netInputs = np.dot(activations, w)

            activations = self.Sigmoid(netInputs)

        return(activations)
    
    def Sigmoid(self, x):
        return (1/(1 + np.exp(-x)))



if __name__ == '__main__':

    temp = MLP(3,3,2)