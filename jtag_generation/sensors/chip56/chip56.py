######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "56"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 159
IVDREF1B = 146
IVDREF1C = 169
IVDREF1D = 137

# Thermal noise: TN
THN_matA = 0.9372
THN_matB = 0.8969
THN_matC = 0.9223
THN_matD = 0.9687

# Fixed pattern noise: FPN
FPN_matA = 0.4059
FPN_matB = 0.4856
FPN_matC = 0.5785
FPN_matD = 0.537

# Offset
OFF_matA = -0.1707
OFF_matB = 0.1656
OFF_matC = 0.0628
OFF_matD = 0.1653

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
