######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "101"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 166
IVDREF1B = 95
IVDREF1C = 140
IVDREF1D = 194

# Thermal noise: TN
THN_matA = 0.982
THN_matB = 0.9574
THN_matC = 0.9588
THN_matD = 0.9306

# Fixed pattern noise: FPN
FPN_matA = 0.4502
FPN_matB = 0.4556
FPN_matC = 0.5325
FPN_matD = 0.4514

# Offset
OFF_matA = -0.2082
OFF_matB = -0.1831
OFF_matC = -0.2023
OFF_matD = -0.1298

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
