import sys
from njlog import RecordFile, StdRecordCode
from njlog.plugins.ssl import *
from njlog.plugins.modbus import *

if len(sys.argv) >= 2:
    path = sys.argv[1]
else:
    path = "./ssl.njlog"

file = RecordFile()
file.open(path)

print("file:", path)
print("    hdr:", file.hdr)
print("    guids:", file.representer_guids)

while record := file.read():
    match record.code:
        case StdRecordCode.Tx:
            print("Outbound data:", record.data)

        case StdRecordCode.Rx:
            print("Inbound data:", record.data)

        case SslLogRecordCode.SslCertificate:
            print("SSL certificate:", record.data)

        case ModbusLogRecordCode.Packet_rtu_master:
            print("Modbus RTU master packet:", record.data)

        case ModbusLogRecordCode.Packet_rtu_slave:
            print("Modbus RTU slave packet:", record.data)

        # ...

        case _:
            print(f"Record 0x{record.code:016x}:", record.data)
