######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "105"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 133
IVDREF1B = 133
IVDREF1C = 123
IVDREF1D = 124

# Thermal noise: TN
THN_matA = 0.8952
THN_matB = 0.919
THN_matC = 0.9009
THN_matD = 0.8696

# Fixed pattern noise: FPN
FPN_matA = 0.3417
FPN_matB = 0.424
FPN_matC = 0.4443
FPN_matD = 0.3797

# Offset
OFF_matA = -0.1403
OFF_matB = -0.1163
OFF_matC = 0.0594
OFF_matD = 0.06079

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
