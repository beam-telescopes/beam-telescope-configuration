######################################
# Last update: 29 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "81"
# Input names
input_folder = "former2015/"
input_file_name = "chip81_thresh"
# columns to disable, if as a list 
DIS_col = []

######################################
# Generate using Jtag class
from generate_jtag import Jtag_update
# Constructor
chip = Jtag_update(sensor_name, input_folder, input_file_name, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)
