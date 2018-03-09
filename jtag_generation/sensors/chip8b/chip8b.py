######################################
# Last update: 08 March 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "8b"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 112
IVDREF1B = 150
IVDREF1C = 103
IVDREF1D = 116

# Thermal noise: TN
THN_matA = 0.9932
THN_matB = 0.9489
THN_matC = 0.9965
THN_matD = 0.8824

# Fixed pattern noise: FPN
FPN_matA = 0.4505
FPN_matB = 0.4817
FPN_matC = 0.5714
FPN_matD = 0.5183

# Offset
OFF_matA = -0.06463
OFF_matB = -0.08043
OFF_matC = -0.2642
OFF_matD = -0.222

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
