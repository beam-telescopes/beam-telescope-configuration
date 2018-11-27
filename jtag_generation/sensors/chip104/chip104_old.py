######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "104"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 96
IVDREF1B = 93
IVDREF1C = 133
IVDREF1D = 210

# Thermal noise: TN
THN_matA = 0.9604
THN_matB = 0.9365
THN_matC = 0.9516
THN_matD = 0.8936

# Fixed pattern noise: FPN
FPN_matA = 0.5125
FPN_matB = 0.4387
FPN_matC = 0.6004
FPN_matD = 0.3796

# Offset
OFF_matA = 0.0005638
OFF_matB = -0.06264
OFF_matC = 0.1124
OFF_matD = 0.2176

# Disable columns/discriminators
DIS_col = [693]

######################################
# Generate using Jtag class
from generate_jtag import Jtag
# Constructor
chip = Jtag(sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)
