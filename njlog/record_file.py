import types
import uuid
import ctypes as C

#
# imported from /scripts/api/log_RecordFile.jnc
#

class RecordFileHdr(C.LittleEndianStructure):
    _fields_ = [
        ("signature", C.c_uint32),
        ("version", C.c_uint32),
        ("record_count", C.c_uint64),
        ("total_record_size", C.c_uint64),
        ("last_record_size", C.c_uint32),
        ("record_offset", C.c_uint32, 24),
        ("aux_representer_count", C.c_uint32, 8),
        ("representer_guid", C.c_uint8 * 16),
    ]

    SIGNATURE = C.c_uint32.from_buffer_copy(b'log:').value


class Record(C.LittleEndianStructure):
    _fields_ = [
        ("signature", C.c_uint32),
        ("data_size", C.c_uint32),
        ("code", C.c_uint64),
        ("timestamp", C.c_uint64),
    ]

    SIGNATURE = C.c_uint32.from_buffer_copy(b'\nrc:').value

#
# RecordFile reads an njlog file record by record
#

class RecordFile:
    def __init__(self):
        self._file = None
        self._hdr = None
        self._representer_guids = None

    @property
    def hdr(self): # return a dictinary made out of ctype struct
        return { f[0]: getattr(self._hdr, f[0]) for f in self._hdr._fields_ }

    @property
    def representer_guids(self):
        return self._representer_guids

    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None

        self._hdr = None
        self._representer_guids = None

    def open(self, path):
        self.close()
        self._file = open(path, "rb")

        block = self._file.read(C.sizeof(RecordFileHdr))
        self._hdr = RecordFileHdr.from_buffer_copy(block)
        aux_representer_size = self._hdr.aux_representer_count * 16
        min_record_offset = C.sizeof(RecordFileHdr) + aux_representer_size

        if self._hdr.signature != RecordFileHdr.SIGNATURE or \
            self._hdr.record_offset < min_record_offset \
        :
            self.close()
            raise ValueError("invalid log record file header")

        representer_guids = [uuid.UUID(bytes_le=bytes(self._hdr.representer_guid))]

        block = self._file.read(aux_representer_size)
        for ofs in range(0, aux_representer_size, 16):
            representer_guids.append(uuid.UUID(bytes_le=bytes(block[ofs:ofs + 16])))

        self._representer_guids = tuple(representer_guids) # to immutable tuple
        self._file.seek(self._hdr.record_offset)

    def read(self):
        record_end_offset = self._hdr.record_offset + self._hdr.total_record_size
        if self._file.tell() >= record_end_offset:
            return None

        block = self._file.read(C.sizeof(Record))
        record = Record.from_buffer_copy(block)
        if record.signature != Record.SIGNATURE:
            raise ValueError("invalid log record")

        record.data = self._file.read(record.data_size) if record.data_size else []
        return record
