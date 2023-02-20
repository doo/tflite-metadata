# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class ExpandDimsOptions(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ExpandDimsOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsExpandDimsOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def ExpandDimsOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed
        )

    # ExpandDimsOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


def ExpandDimsOptionsStart(builder):
    builder.StartObject(0)


def Start(builder):
    return ExpandDimsOptionsStart(builder)


def ExpandDimsOptionsEnd(builder):
    return builder.EndObject()


def End(builder):
    return ExpandDimsOptionsEnd(builder)


class ExpandDimsOptionsT(object):

    # ExpandDimsOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        expandDimsOptions = ExpandDimsOptions()
        expandDimsOptions.Init(buf, pos)
        return cls.InitFromObj(expandDimsOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, expandDimsOptions):
        x = ExpandDimsOptionsT()
        x._UnPack(expandDimsOptions)
        return x

    # ExpandDimsOptionsT
    def _UnPack(self, expandDimsOptions):
        if expandDimsOptions is None:
            return

    # ExpandDimsOptionsT
    def Pack(self, builder):
        ExpandDimsOptionsStart(builder)
        expandDimsOptions = ExpandDimsOptionsEnd(builder)
        return expandDimsOptions