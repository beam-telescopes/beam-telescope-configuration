######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "5b"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 110
IVDREF1B = 188
IVDREF1C = 159
IVDREF1D = 101
# Thermal noise: TN
THN_matA = 0.961 
THN_matB = 0.8876
THN_matC = 0.954
THN_matD = 0.8724
# Fixed pattern noise: FPN
FPN_matA = 0.4745
FPN_matB = 0.4491
FPN_matC = 0.5235
FPN_matD = 0.5894
# Offset
OFF_matA = 0.5848
OFF_matB = 0.4153
OFF_matC = 0.4551
OFF_matD = 0.4008
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

