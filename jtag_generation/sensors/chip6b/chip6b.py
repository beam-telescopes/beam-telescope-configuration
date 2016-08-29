######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "6b"

# Middlepoints in DAC
IVDREF2  = 98 
IVDREF1A = 145
IVDREF1B = 98
IVDREF1C = 179
IVDREF1D = 171
# Thermal noise: TN
THN_matA = 0.9837
THN_matB = 0.874
THN_matC = 0.879
THN_matD = 0.8984
# Fixed pattern noise: FPN
FPN_matA = 0.4603
FPN_matB = 0.4334
FPN_matC = 0.4559
FPN_matD = 0.4604
# Offset
OFF_matA = -0.1641
OFF_matB = -0.01736
OFF_matC = 0.021
OFF_matD = 0.01869
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

