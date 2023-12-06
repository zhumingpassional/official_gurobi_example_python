#!/usr/bin/env python3.9

# Copyright 2023, Gurobi Optimization, LLC

#  This example reads a model from a file and tunes it.
#  It then writes the best parameter settings to a file
#  and solves the model using these parameters.

import sys
import gurobipy as gp

if len(sys.argv) < 2:
    print('Usage: tune.py filename')
    sys.exit(0)

# Read the model
model = gp.read(sys.argv[1])

# Set the TuneResults parameter to 1
model.Params.TuneResults = 1

# Tune the model
model.tune()

if model.TuneResultCount > 0:

    # Load the best tuned parameters into the model
    model.getTuneResult(0)

    # Write tuned parameters to a file
    model.write('tune.prm')

    # Solve the model using the tuned parameters
    model.optimize()
