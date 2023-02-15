# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AudioProperties(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AudioProperties()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAudioProperties(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def AudioPropertiesBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4D\x30\x30\x31", size_prefixed=size_prefixed)

    # AudioProperties
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AudioProperties
    def SampleRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # AudioProperties
    def Channels(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def AudioPropertiesStart(builder): builder.StartObject(2)
def Start(builder):
    return AudioPropertiesStart(builder)
def AudioPropertiesAddSampleRate(builder, sampleRate): builder.PrependUint32Slot(0, sampleRate, 0)
def AddSampleRate(builder, sampleRate):
    return AudioPropertiesAddSampleRate(builder, sampleRate)
def AudioPropertiesAddChannels(builder, channels): builder.PrependUint32Slot(1, channels, 0)
def AddChannels(builder, channels):
    return AudioPropertiesAddChannels(builder, channels)
def AudioPropertiesEnd(builder): return builder.EndObject()
def End(builder):
    return AudioPropertiesEnd(builder)