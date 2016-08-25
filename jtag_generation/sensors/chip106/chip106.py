######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "106"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 141
IVDREF1B = 138
IVDREF1C = 130
IVDREF1D = 140

# Thermal noise: TN
THN_matA = 1.003
THN_matB = 0.9419
THN_matC = 0.9264
THN_matD = 0.9433

# Fixed pattern noise: FPN
FPN_matA = 0.5155
FPN_matB = 0.4697
FPN_matC = 0.5455
FPN_matD = 0.5313

# Offset
OFF_matA = -0.09608
OFF_matB = 0.02458
OFF_matC = -0.1368
OFF_matD = 0.1569

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
