# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OneHotOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OneHotOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOneHotOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def OneHotOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # OneHotOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OneHotOptions
    def Axis(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def OneHotOptionsStart(builder): builder.StartObject(1)
def Start(builder):
    return OneHotOptionsStart(builder)
def OneHotOptionsAddAxis(builder, axis): builder.PrependInt32Slot(0, axis, 0)
def AddAxis(builder, axis):
    return OneHotOptionsAddAxis(builder, axis)
def OneHotOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return OneHotOptionsEnd(builder)

class OneHotOptionsT(object):

    # OneHotOptionsT
    def __init__(self):
        self.axis = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        oneHotOptions = OneHotOptions()
        oneHotOptions.Init(buf, pos)
        return cls.InitFromObj(oneHotOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, oneHotOptions):
        x = OneHotOptionsT()
        x._UnPack(oneHotOptions)
        return x

    # OneHotOptionsT
    def _UnPack(self, oneHotOptions):
        if oneHotOptions is None:
            return
        self.axis = oneHotOptions.Axis()

    # OneHotOptionsT
    def Pack(self, builder):
        OneHotOptionsStart(builder)
        OneHotOptionsAddAxis(builder, self.axis)
        oneHotOptions = OneHotOptionsEnd(builder)
        return oneHotOptions
