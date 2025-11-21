import enum
from ..record_code import RecordCodeFlags

#
# imported from /scripts/plugins/Modbus/ModbusLogRecordCode.jnc
#

class ModbusLogRecordCode(enum.IntEnum):
    ParseError          = 0x01da92357a7ca801
    Packet_rtu_master   = 0x01da92357a7ca802 | RecordCodeFlags.Foldable
    Packet_rtu_slave    = 0x01da92357a7ca803 | RecordCodeFlags.Foldable
    Packet_ascii_master = 0x01da92357a7ca804 | RecordCodeFlags.Foldable
    Packet_ascii_slave  = 0x01da92357a7ca805 | RecordCodeFlags.Foldable
    Packet_tcp_master   = 0x01da92357a7ca806 | RecordCodeFlags.Foldable
    Packet_tcp_slave    = 0x01da92357a7ca807 | RecordCodeFlags.Foldable
