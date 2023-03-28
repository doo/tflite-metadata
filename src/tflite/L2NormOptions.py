# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class L2NormOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = L2NormOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsL2NormOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def L2NormOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # L2NormOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # L2NormOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def L2NormOptionsStart(builder): builder.StartObject(1)
def Start(builder):
    return L2NormOptionsStart(builder)
def L2NormOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def AddFusedActivationFunction(builder, fusedActivationFunction):
    return L2NormOptionsAddFusedActivationFunction(builder, fusedActivationFunction)
def L2NormOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return L2NormOptionsEnd(builder)

class L2NormOptionsT(object):

    # L2NormOptionsT
    def __init__(self):
        self.fusedActivationFunction = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        l2NormOptions = L2NormOptions()
        l2NormOptions.Init(buf, pos)
        return cls.InitFromObj(l2NormOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, l2NormOptions):
        x = L2NormOptionsT()
        x._UnPack(l2NormOptions)
        return x

    # L2NormOptionsT
    def _UnPack(self, l2NormOptions):
        if l2NormOptions is None:
            return
        self.fusedActivationFunction = l2NormOptions.FusedActivationFunction()

    # L2NormOptionsT
    def Pack(self, builder):
        L2NormOptionsStart(builder)
        L2NormOptionsAddFusedActivationFunction(builder, self.fusedActivationFunction)
        l2NormOptions = L2NormOptionsEnd(builder)
        return l2NormOptions
