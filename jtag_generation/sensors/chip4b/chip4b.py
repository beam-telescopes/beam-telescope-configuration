######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "4b"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 132
IVDREF1B = 167
IVDREF1C = 116
IVDREF1D = 185
# Thermal noise: TN
THN_matA = 0.9606 
THN_matB = 0.8968
THN_matC = 0.9802
THN_matD = 0.9279
# Fixed pattern noise: FPN
FPN_matA = 0.4428
FPN_matB = 0.3595
FPN_matC = 0.5626
FPN_matD = 0.4931
# Offset
OFF_matA = 0.3676
OFF_matB = 0.2016
OFF_matC = 0.353
OFF_matD = 0.3459
# columns to disable, if as a list 
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
