from sklearn import tree
import numpy as np

import matplotlib.pylab as plt


import sys



def read_jets():
    # Read in the jet info for this event.
    not_at_end = True
   
    f = open('mc_wjets.txt')
    while(not_at_end):
        line = f.readline()
        if line=="":
            not_at_end = False
    
        if line.find("Event")>=0:
            new_event = True
    
        if new_event==True:
            jets = []
            line = f.readline()
            njets = int(line)
            for i in xrange(njets):
                line = f.readline()
                vals = line.split()
                e = float(vals[0])
                px = float(vals[1])
                py = float(vals[2])
                pz = float(vals[3])
                bquark_jet_tag = float(vals[4])
                jets.append([e,px,py,pz,bquark_jet_tag])
                
                    
        line = f.readline()
        vals = line.split()
        new_event = False
            
    return jets

def read_ttbar():
    not_at_end = True
    
    f = open('mc_ttbar.txt')
    while(not_at_end):
        line = f.readline()
        if line=="":
            not_at_end = False
        
        if line.find("Event")>=0:
            new_event = True
        
        if new_event==True:
            muons = []
            line = f.readline()
            nmuons = int(line)
            for i in xrange(nmuons):
                line = f.readline()
                vals = line.split()
                e = float(vals[0])
                px = float(vals[1])
                py = float(vals[2])
                pz = float(vals[3])
                charge = float(vals[4])
                muons.append([e,px,py,pz,charge])

        line = f.readline()
        vals = line.split()
        new_event = False
    return muons

# Obtain our training sample of 500 events from each dataset
d_jets = read_jets()
d_ttbar = read_ttbar()
tSample_jets = d_jets[:501]
tSample_muons = d_ttbar[:501]

# Combine the training samples to one dataset
tSample = tSample_jets.extend(tSample_muons)

# Create the DT Classifier
dt_classifier = tree.DecisionTreeClassifier()

# Make it learn
#dt_classifier = dt_classifier.fit(tSample)


print tSample