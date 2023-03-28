# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ATan2Options(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ATan2Options()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsATan2Options(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ATan2OptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # ATan2Options
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def ATan2OptionsStart(builder): builder.StartObject(0)
def Start(builder):
    return ATan2OptionsStart(builder)
def ATan2OptionsEnd(builder): return builder.EndObject()
def End(builder):
    return ATan2OptionsEnd(builder)

class ATan2OptionsT(object):

    # ATan2OptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        atan2Options = ATan2Options()
        atan2Options.Init(buf, pos)
        return cls.InitFromObj(atan2Options)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, atan2Options):
        x = ATan2OptionsT()
        x._UnPack(atan2Options)
        return x

    # ATan2OptionsT
    def _UnPack(self, atan2Options):
        if atan2Options is None:
            return

    # ATan2OptionsT
    def Pack(self, builder):
        ATan2OptionsStart(builder)
        atan2Options = ATan2OptionsEnd(builder)
        return atan2Options
