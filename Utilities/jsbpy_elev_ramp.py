import jsbsim as jsb

fdm = jsb.FGFDMExec('.', None) # Create FGFDMExec model

fdm.load_model('c172r') # Load example aircraft (Cessna 172)

# Set initial conditions
fdm.load_ic('reset00', True)
fdm.run_ic()

fdm.print_property_catalog() # Print property catalog

# Simulation loop 
elev_cmd = fdm.get_property_value('fcs/elevator-cmd-norm')
print('Ramping Elevator...')
while fdm.run() and elev_cmd < 1:
    print(fdm.get_property_value('fcs/pitch-trim-sum'))
    if fdm.get_sim_time() >= 0.1:
        new_val = elev_cmd+0.001
        fdm.set_property_value('fcs/elevator-cmd-norm',new_val)
    fdm.get_sim_time()
    elev_cmd = fdm.get_property_value('fcs/elevator-cmd-norm')
    pass
