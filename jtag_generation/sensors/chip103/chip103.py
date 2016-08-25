######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "103"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 84
IVDREF1B = 124
IVDREF1C = 131
IVDREF1D = 150

# Thermal noise: TN
THN_matA = 0.9755
THN_matB = 0.9017
THN_matC = 1.006
THN_matD = 0.9653

# Fixed pattern noise: FPN
FPN_matA = 0.4206
FPN_matB = 0.3875
FPN_matC = 0.496
FPN_matD = 0.5335

# Offset
OFF_matA = 0.06238
OFF_matB = 0.3005
OFF_matC = -0.1702
OFF_matD = 0.1174

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
