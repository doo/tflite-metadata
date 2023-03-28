# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Metadata(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Metadata()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMetadata(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def MetadataBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # Metadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Metadata
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Metadata
    def Buffer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def MetadataStart(builder): builder.StartObject(2)
def Start(builder):
    return MetadataStart(builder)
def MetadataAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return MetadataAddName(builder, name)
def MetadataAddBuffer(builder, buffer): builder.PrependUint32Slot(1, buffer, 0)
def AddBuffer(builder, buffer):
    return MetadataAddBuffer(builder, buffer)
def MetadataEnd(builder): return builder.EndObject()
def End(builder):
    return MetadataEnd(builder)

class MetadataT(object):

    # MetadataT
    def __init__(self):
        self.name = None  # type: str
        self.buffer = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        metadata = Metadata()
        metadata.Init(buf, pos)
        return cls.InitFromObj(metadata)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, metadata):
        x = MetadataT()
        x._UnPack(metadata)
        return x

    # MetadataT
    def _UnPack(self, metadata):
        if metadata is None:
            return
        self.name = metadata.Name()
        self.buffer = metadata.Buffer()

    # MetadataT
    def Pack(self, builder):
        if self.name is not None:
            name = builder.CreateString(self.name)
        MetadataStart(builder)
        if self.name is not None:
            MetadataAddName(builder, name)
        MetadataAddBuffer(builder, self.buffer)
        metadata = MetadataEnd(builder)
        return metadata
