# Neural Network

import numpy as np
import scipy.special


class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learning_rate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learning_rate


        # The outer weights-hidden weights
        self.wih = np.random.uniform(0.0, pow(self.hnodes, -0.5),
                                     (self.hnodes, self.inodes))

        # The hidden weights - outer weights
        self.who = np.random.uniform(1.0, pow(self.onodes, -0.5),
                                     (self.onodes, self.hnodes))
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    def train(self, input_list, target_list):
        inputs = np.array(input_list, ndmin=2).T
        targets = np.array(output_list, ndmin=2).T

        hidden_inputs = np.dot(self.wih, inputs)

        #Adding the activation function to the hidden layers
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(hidden_outputs, self.who)

        final_outputs = self.activation_function(final_inputs)

        # Error
        Error_output = targets - final_outputs

        Hidden_errors = np.dot(self.who.T, Error_output)
        
        # Update the weights: Hidden and Output layers
        self.who += self.lr*np.dot((Error_output*final_outputs*
                                    (1.0-final_outputs)),
                                   np.transpose(hidden_outputs))

        # Update the weights: Input and Hidden layers
        self.wih += self.lr*np.dot((Hidden_errors*hidden_outputs*
                                    (1.0-hidden_outputs)),
                                   np.transpose(inputs))

        pass

    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
        

    

        

        
             
    
