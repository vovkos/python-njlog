import enum
from ..record_code import RecordCodeFlags, PartCodeFlags

#
# imported from /scripts/plugins/SocketLog/SocketLogRecordCode.jnc
#

class SocketLogRecordCode(enum.IntEnum):
    Open               = 0x01d483f3e69da200
    OpenError          = 0x01d483f3e69da201
    Close              = 0x01d483f3e69da202
    Resolving          = 0x01d483f3e69da203
    Connecting         = 0x01d483f3e69da204
    ConnectingFrom     = 0x01d483f3e69da205
    ResolveCompleted   = 0x01d483f3e69da206
    ConnectCompleted   = 0x01d483f3e69da207
    ConnectCancelled   = 0x01d483f3e69da208
    ConnectError       = 0x01d483f3e69da209
    Disconnected       = 0x01d483f3e69da20a
    Disconnected_old   = 0x01d483f3e69da20b
    ResolveCancelled   = ConnectCancelled
    ResolveError       = ConnectError
    ReconnectDelay     = 0x01d483f3e69da212
    Listening          = 0x01d483f3e69da20c
    ListenError        = 0x01d483f3e69da20d
    ListenStopped      = 0x01d483f3e69da20e
    ClientConnected    = 0x01d483f3e69da20f
    ClientDisconnected = 0x01d483f3e69da210
    ClientRejected     = 0x01d483f3e69da211
    ClientChanged      = 0x01d483f3e69da213
    ClientRemoved      = 0x01d483f3e69da214
    ResolveCompletedPrefix = 0x01d483f3e69da215
    ConnectCompletedPrefix = 0x01d483f3e69da216
    DisconnectDataPending  = 0x01d483f3e69da217


class SocketLogPartCode(enum.IntEnum):
    Connecting       = 0x01d483f3e69da203 | PartCodeFlags.MergeableForward
    ConnectCompleted = 0x01d483f3e69da203 | PartCodeFlags.MergeableBackward


class TcpDisconnectLogRecordFlags(enum.IntEnum):
    Remote     = 0x01
    Reset      = 0x02
    KeepClient = 0x04
