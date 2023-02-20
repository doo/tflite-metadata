# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class GeluOptions(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GeluOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGeluOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def GeluOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed
        )

    # GeluOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GeluOptions
    def Approximate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False


def GeluOptionsStart(builder):
    builder.StartObject(1)


def Start(builder):
    return GeluOptionsStart(builder)


def GeluOptionsAddApproximate(builder, approximate):
    builder.PrependBoolSlot(0, approximate, 0)


def AddApproximate(builder, approximate):
    return GeluOptionsAddApproximate(builder, approximate)


def GeluOptionsEnd(builder):
    return builder.EndObject()


def End(builder):
    return GeluOptionsEnd(builder)


class GeluOptionsT(object):

    # GeluOptionsT
    def __init__(self):
        self.approximate = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        geluOptions = GeluOptions()
        geluOptions.Init(buf, pos)
        return cls.InitFromObj(geluOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, geluOptions):
        x = GeluOptionsT()
        x._UnPack(geluOptions)
        return x

    # GeluOptionsT
    def _UnPack(self, geluOptions):
        if geluOptions is None:
            return
        self.approximate = geluOptions.Approximate()

    # GeluOptionsT
    def Pack(self, builder):
        GeluOptionsStart(builder)
        GeluOptionsAddApproximate(builder, self.approximate)
        geluOptions = GeluOptionsEnd(builder)
        return geluOptions