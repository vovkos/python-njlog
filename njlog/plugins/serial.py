import enum
import ctypes as C
from ..record_code import RecordCodeFlags

#
# imported from /scripts/plugins/SerialLog/SerialLogRecordCode.jnc
#

class SerialLogRecordCode(enum.IntEnum):
    PortOpened            = 0x01d47c8fc7b0f700 | RecordCodeFlags.Foldable
    PortOpened_old        = 0x01d47c8fc7b0f701 | RecordCodeFlags.Foldable
    PortOpenError         = 0x01d47c8fc7b0f702
    PortClosedNamed       = 0x01d47c8fc7b0f703
    BaudRateChanged       = 0x01d47c8fc7b0f704
    DataBitsChanged       = 0x01d47c8fc7b0f705
    StopBitsChanged       = 0x01d47c8fc7b0f706
    ParityChanged         = 0x01d47c8fc7b0f707
    FlowControlChanged    = 0x01d47c8fc7b0f708
    RtsChanged            = 0x01d47c8fc7b0f709
    DtrChanged            = 0x01d47c8fc7b0f70a
    StatusLineChanged     = 0x01d47c8fc7b0f70b
    ReadModeChanged       = 0x01d47c8fc7b0f70c
    ReadIntervalChanged   = 0x01d47c8fc7b0f70d
    BuggyDriverDetected   = 0x01d47c8fc7b0f70e
    ControlLineChanged    = 0x01d47c8fc7b0f70f
    LineError             = 0x01d47c8fc7b0f710
    BreakConditionChanged = 0x01d47c8fc7b0f711
    PortClosed            = 0x01d47c8fc7b0f712
    PortOpenedEx          = 0x01d47c8fc7b0f713 | RecordCodeFlags.Foldable
    CaptureStarted        = 0x01d47c8fc7b0f714 | RecordCodeFlags.Foldable
    UpdateIntervalChanged = 0x01d47c8fc7b0f715


class SerialReadMode(enum.IntEnum):
    CheckComstat   = 0,
    WaitFirstChar  = 1,
    IntervalBased  = 2,


class SerialOpenParams(C.LittleEndianStructure):
    _fields_ = [
        ( "m_baudRate", C.c_uint32 ),
        ( "m_flowControl", C.c_uint32 ),
        ( "m_dataBits", C.c_uint32 ),
        ( "m_stopBits", C.c_uint32 ),
        ( "m_parity", C.c_uint32 ),
        ( "m_readInterval", C.c_uint32 ),
        ( "m_dtr", C.c_uint8 ),
        ( "m_rts", C.c_uint8 ),
        ( "m_statusLines", C.c_uint32 ),
        ( "m_options", C.c_uint32 ),
        ( "m_osKind", C.c_uint32 ),
    ]


class SerialStatusLineChangedParams(C.LittleEndianStructure):
    _fields_ = [
        ( "m_lines", C.c_uint32 ),
        ( "m_mask", C.c_uint32 ),
    ]
