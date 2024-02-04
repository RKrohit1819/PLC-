
import snap7
from snap7.util import *
from snap7.common import S7AreaDB

plc = snap7.client.Client()
plc.connect('192.168.1.34', 0, 1)

# Read the contents of a DB block
block_num = 1
byte_offset = 0
byte_count = 100
data = plc.read_area(snap7.types.AREA_DB, block_num, byte_offset, byte_count)
# Convert the raw data to a Python list
data_list = snap7.util.get_real_array(data, 0, byte_count)
# Print the contents of the DB block
print(data_list)
