import enum
from ..record_code import RecordCodeFlags

#
# imported from /scripts/plugins/SslLog/SslLogRecordCode.jnc
#

class SslLogRecordCode(enum.IntEnum):
    SslHandshaking         = 0x01d5cdeded08f700
    SslHandshakeCompleted  = 0x01d5cdeded08f701
    SslCertificate         = 0x01d5cdeded08f702 | RecordCodeFlags.Foldable
    SslCipher              = 0x01d5cdeded08f703
    SslConnectCompleted    = 0x01d5cdeded08f704
