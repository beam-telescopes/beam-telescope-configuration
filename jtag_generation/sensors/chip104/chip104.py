######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "104"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 65
IVDREF1B = 80
IVDREF1C = 135
IVDREF1D = 145

# Thermal noise: TN
THN_matA = 0.9318
THN_matB = 0.8521
THN_matC = 0.8079
THN_matD = 0.8679

# Fixed pattern noise: FPN
FPN_matA = 0.4042
FPN_matB = 0.4578
FPN_matC = 0.5161
FPN_matD = 0.5197

# Offset
OFF_matA = -0.4058
OFF_matB = -0.0084
OFF_matC = 0.2322
OFF_matD = 0.1061

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
