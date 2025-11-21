import ctypes as C
from .record_file import Record

#
# RecordStream parses a stream of log records chunk by chunk
#

class RecordStream:
    def __init__(self):
        self._buffer = bytearray()
        self._record = None

    @property
    def record_count(self):
        return self._record_count

    def reset():
        self._buffer.clear()
        self._record = None

    def parse(self, chunk):
        self._buffer.extend(chunk)
        records = []

        while True:
            if self._record is None:
                if len(self._buffer) < C.sizeof(Record):
                    break

                self._record = Record.from_buffer_copy(Record, self._buffer)
                if self._record.signature != Record.SIGNATURE:
                    raise ValueError("invalid record signature")

                del self._buffer[:C.sizeof(Record)]

            if len(self._buffer) < self._record.data_size:
                break

            self._record.data = bytes(self._buffer[0:self._record.data_size])
            del self._buffer[:self._record.data_size]
            records.append(self._record)
            self._record = None

        return records
