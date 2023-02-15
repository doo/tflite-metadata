# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TransposeConvOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TransposeConvOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTransposeConvOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def TransposeConvOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # TransposeConvOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TransposeConvOptions
    def Padding(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # TransposeConvOptions
    def StrideW(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TransposeConvOptions
    def StrideH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TransposeConvOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def TransposeConvOptionsStart(builder): builder.StartObject(4)
def Start(builder):
    return TransposeConvOptionsStart(builder)
def TransposeConvOptionsAddPadding(builder, padding): builder.PrependInt8Slot(0, padding, 0)
def AddPadding(builder, padding):
    return TransposeConvOptionsAddPadding(builder, padding)
def TransposeConvOptionsAddStrideW(builder, strideW): builder.PrependInt32Slot(1, strideW, 0)
def AddStrideW(builder, strideW):
    return TransposeConvOptionsAddStrideW(builder, strideW)
def TransposeConvOptionsAddStrideH(builder, strideH): builder.PrependInt32Slot(2, strideH, 0)
def AddStrideH(builder, strideH):
    return TransposeConvOptionsAddStrideH(builder, strideH)
def TransposeConvOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(3, fusedActivationFunction, 0)
def AddFusedActivationFunction(builder, fusedActivationFunction):
    return TransposeConvOptionsAddFusedActivationFunction(builder, fusedActivationFunction)
def TransposeConvOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return TransposeConvOptionsEnd(builder)

class TransposeConvOptionsT(object):

    # TransposeConvOptionsT
    def __init__(self):
        self.padding = 0  # type: int
        self.strideW = 0  # type: int
        self.strideH = 0  # type: int
        self.fusedActivationFunction = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        transposeConvOptions = TransposeConvOptions()
        transposeConvOptions.Init(buf, pos)
        return cls.InitFromObj(transposeConvOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, transposeConvOptions):
        x = TransposeConvOptionsT()
        x._UnPack(transposeConvOptions)
        return x

    # TransposeConvOptionsT
    def _UnPack(self, transposeConvOptions):
        if transposeConvOptions is None:
            return
        self.padding = transposeConvOptions.Padding()
        self.strideW = transposeConvOptions.StrideW()
        self.strideH = transposeConvOptions.StrideH()
        self.fusedActivationFunction = transposeConvOptions.FusedActivationFunction()

    # TransposeConvOptionsT
    def Pack(self, builder):
        TransposeConvOptionsStart(builder)
        TransposeConvOptionsAddPadding(builder, self.padding)
        TransposeConvOptionsAddStrideW(builder, self.strideW)
        TransposeConvOptionsAddStrideH(builder, self.strideH)
        TransposeConvOptionsAddFusedActivationFunction(builder, self.fusedActivationFunction)
        transposeConvOptions = TransposeConvOptionsEnd(builder)
        return transposeConvOptions
