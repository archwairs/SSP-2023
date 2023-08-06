# SSP-2023

'poly_with_sol (good).lmp' is the LAMMPS file that is used to simulate a homopolymer in a good solvent.
'poly_with_sol (poor).lmp' is the LAMMPS file that is used to simulate a homopolymer in a poor solvent.
'create_polymer.py' is a python script used to generate atom and bond data (in the 'full' atom format), that is fed into the the LAMMPS files using the 'read_data' command.
'calc_rog.py' is used to calculate the radius of gyration of the polymer in equilibrium, using .xyz file as input.
'R_gN.py' plots the radius of gyration with the number of monomers of the polymer, and find the best-fit polynomial.
