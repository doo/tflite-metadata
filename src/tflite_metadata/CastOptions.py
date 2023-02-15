# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CastOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CastOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCastOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def CastOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # CastOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CastOptions
    def InDataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # CastOptions
    def OutDataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def CastOptionsStart(builder): builder.StartObject(2)
def Start(builder):
    return CastOptionsStart(builder)
def CastOptionsAddInDataType(builder, inDataType): builder.PrependInt8Slot(0, inDataType, 0)
def AddInDataType(builder, inDataType):
    return CastOptionsAddInDataType(builder, inDataType)
def CastOptionsAddOutDataType(builder, outDataType): builder.PrependInt8Slot(1, outDataType, 0)
def AddOutDataType(builder, outDataType):
    return CastOptionsAddOutDataType(builder, outDataType)
def CastOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return CastOptionsEnd(builder)

class CastOptionsT(object):

    # CastOptionsT
    def __init__(self):
        self.inDataType = 0  # type: int
        self.outDataType = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        castOptions = CastOptions()
        castOptions.Init(buf, pos)
        return cls.InitFromObj(castOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, castOptions):
        x = CastOptionsT()
        x._UnPack(castOptions)
        return x

    # CastOptionsT
    def _UnPack(self, castOptions):
        if castOptions is None:
            return
        self.inDataType = castOptions.InDataType()
        self.outDataType = castOptions.OutDataType()

    # CastOptionsT
    def Pack(self, builder):
        CastOptionsStart(builder)
        CastOptionsAddInDataType(builder, self.inDataType)
        CastOptionsAddOutDataType(builder, self.outDataType)
        castOptions = CastOptionsEnd(builder)
        return castOptions
