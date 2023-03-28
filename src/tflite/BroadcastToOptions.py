# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BroadcastToOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BroadcastToOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBroadcastToOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def BroadcastToOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # BroadcastToOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def BroadcastToOptionsStart(builder): builder.StartObject(0)
def Start(builder):
    return BroadcastToOptionsStart(builder)
def BroadcastToOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return BroadcastToOptionsEnd(builder)

class BroadcastToOptionsT(object):

    # BroadcastToOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        broadcastToOptions = BroadcastToOptions()
        broadcastToOptions.Init(buf, pos)
        return cls.InitFromObj(broadcastToOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, broadcastToOptions):
        x = BroadcastToOptionsT()
        x._UnPack(broadcastToOptions)
        return x

    # BroadcastToOptionsT
    def _UnPack(self, broadcastToOptions):
        if broadcastToOptions is None:
            return

    # BroadcastToOptionsT
    def Pack(self, builder):
        BroadcastToOptionsStart(builder)
        broadcastToOptions = BroadcastToOptionsEnd(builder)
        return broadcastToOptions
