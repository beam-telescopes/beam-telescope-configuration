######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "57"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 146
IVDREF1B = 155
IVDREF1C = 211
IVDREF1D = 120

# Thermal noise: TN
THN_matA = 1.021
THN_matB = 0.9632
THN_matC = 1.063
THN_matD = 0.973

# Fixed pattern noise: FPN
FPN_matA = 0.7374
FPN_matB = 0.7343
FPN_matC = 0.8233
FPN_matD = 0.9442

# Offset
OFF_matA = -0.1049
OFF_matB = -0.0658
OFF_matC = -0.346
OFF_matD = -0.0825

# Disable columns/discriminators
DIS_col = []

######################################
# Generate using Jtag class
from generate_jtag import Jtag
# Constructor
chip = Jtag(sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)
