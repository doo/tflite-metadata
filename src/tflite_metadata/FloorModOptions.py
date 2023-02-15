# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FloorModOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FloorModOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFloorModOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def FloorModOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # FloorModOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def FloorModOptionsStart(builder): builder.StartObject(0)
def Start(builder):
    return FloorModOptionsStart(builder)
def FloorModOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return FloorModOptionsEnd(builder)

class FloorModOptionsT(object):

    # FloorModOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        floorModOptions = FloorModOptions()
        floorModOptions.Init(buf, pos)
        return cls.InitFromObj(floorModOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, floorModOptions):
        x = FloorModOptionsT()
        x._UnPack(floorModOptions)
        return x

    # FloorModOptionsT
    def _UnPack(self, floorModOptions):
        if floorModOptions is None:
            return

    # FloorModOptionsT
    def Pack(self, builder):
        FloorModOptionsStart(builder)
        floorModOptions = FloorModOptionsEnd(builder)
        return floorModOptions
