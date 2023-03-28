# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WhereOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WhereOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWhereOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def WhereOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # WhereOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def WhereOptionsStart(builder): builder.StartObject(0)
def Start(builder):
    return WhereOptionsStart(builder)
def WhereOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return WhereOptionsEnd(builder)

class WhereOptionsT(object):

    # WhereOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        whereOptions = WhereOptions()
        whereOptions.Init(buf, pos)
        return cls.InitFromObj(whereOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, whereOptions):
        x = WhereOptionsT()
        x._UnPack(whereOptions)
        return x

    # WhereOptionsT
    def _UnPack(self, whereOptions):
        if whereOptions is None:
            return

    # WhereOptionsT
    def Pack(self, builder):
        WhereOptionsStart(builder)
        whereOptions = WhereOptionsEnd(builder)
        return whereOptions
