######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "69"

# Middlepoints in DAC
IVDREF2  = 98 
IVDREF1A = 102
IVDREF1B = 135
IVDREF1C = 180
IVDREF1D = 194

# Thermal noise: TN
THN_matA = 1.01
THN_matB = 0.952
THN_matC = 0.9628
THN_matD = 0.8984

# Fixed pattern noise: FPN
FPN_matA = 0.4603
FPN_matB = 0.4708
FPN_matC = 0.4589
FPN_matD = 0.448

# Offset
OFF_matA = 0.4928
OFF_matB = 0.4403
OFF_matC = 0.3484
OFF_matD = 0.4998

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
