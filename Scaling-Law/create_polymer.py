import random

def generate_polymer_data_file(num_chains, chain_length, box_size):
    with open('poly_n_full.data', 'w') as f:            #replace n with number of monomers in a chain
        f.write('LAMMPS polymer data file\n\n')
        
        # Header section
        f.write(f'{num_chains * chain_length} atoms\n')
        f.write(f'{chain_length - 1} bonds\n')
        f.write('\n')
        
        # Atom section
        f.write('1 atom types\n')
        f.write('1 bond types\n')
        f.write('\n')
        
        # Box size section
        f.write(f'0.0 {box_size[0]} xlo xhi\n')
        f.write(f'0.0 {box_size[1]} ylo yhi\n')
        f.write(f'0.0 {box_size[2]} zlo zhi\n')
        f.write('\n')
        
        # Mass section
        f.write('Masses\n\n')
        f.write('1 1.0\n')
        f.write('\n')
        
        # Atoms section
        f.write('Atoms\n\n')
        atom_id = 1
        for chain_id in range(num_chains):
            for i in range(chain_length):
                x = 0.8
                y = 1
                z = 10
                x1 = i*x
                y1 = i*y%2
                f.write(f'{str(atom_id).ljust(8)} {str(chain_id + 1).ljust(8)}{str(1).ljust(8)} {str(0).ljust(8)} {str(x1).ljust(8)} {str(y1).ljust(8)} {str(z).ljust(8)}\n')
                atom_id += 1
        f.write('\n')
        
        # Bonds section
        f.write('Bonds\n\n')
        bond_id = 1
        for chain_id in range(num_chains):
            for i in range(chain_length - 1):
                atom1 = (chain_id * chain_length) + i + 1
                atom2 = (chain_id * chain_length) + i + 2
                f.write(f'{str(bond_id).rjust(8)}        1 {str(atom1).rjust(8)} {str(atom2).rjust(8)}\n')
                bond_id += 1

# Example usage
generate_polymer_data_file(1, n, (L_x,L_y,L_z))  #replace L_x, L_y and L_z with dimensions of region of simulation
