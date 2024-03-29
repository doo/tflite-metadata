# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FeatureProperties(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FeatureProperties()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFeatureProperties(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def FeaturePropertiesBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4D\x30\x30\x31", size_prefixed=size_prefixed)

    # FeatureProperties
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def FeaturePropertiesStart(builder): builder.StartObject(0)
def Start(builder):
    return FeaturePropertiesStart(builder)
def FeaturePropertiesEnd(builder): return builder.EndObject()
def End(builder):
    return FeaturePropertiesEnd(builder)

class FeaturePropertiesT(object):

    # FeaturePropertiesT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        featureProperties = FeatureProperties()
        featureProperties.Init(buf, pos)
        return cls.InitFromObj(featureProperties)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, featureProperties):
        x = FeaturePropertiesT()
        x._UnPack(featureProperties)
        return x

    # FeaturePropertiesT
    def _UnPack(self, featureProperties):
        if featureProperties is None:
            return

    # FeaturePropertiesT
    def Pack(self, builder):
        FeaturePropertiesStart(builder)
        featureProperties = FeaturePropertiesEnd(builder)
        return featureProperties
