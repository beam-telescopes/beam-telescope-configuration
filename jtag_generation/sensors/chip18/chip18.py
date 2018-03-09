######################################
# Last update: 08 March 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "18"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 162
IVDREF1B = 123
IVDREF1C = 120
IVDREF1D = 211

# Thermal noise: TN
THN_matA = 1.034
THN_matB = 0.9031
THN_matC = 0.9543
THN_matD = 0.9679

# Fixed pattern noise: FPN
FPN_matA = 0.3453
FPN_matB = 0.536
FPN_matC = 0.6778
FPN_matD = 0.7004

# Offset
OFF_matA = -0.01072
OFF_matB = -0.1301
OFF_matC = -0.039
OFF_matD = -0.04197

# Disable columns/discriminators
DIS_col = [812]

######################################
# Generate using Jtag class
from generate_jtag import Jtag
# Constructor
chip = Jtag(sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)
