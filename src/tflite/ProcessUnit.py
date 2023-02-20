# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class ProcessUnit(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ProcessUnit()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsProcessUnit(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def ProcessUnitBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x4D\x30\x30\x31", size_prefixed=size_prefixed
        )

    # ProcessUnit
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ProcessUnit
    def OptionsType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # ProcessUnit
    def Options(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table

            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None


def ProcessUnitStart(builder):
    builder.StartObject(2)


def Start(builder):
    return ProcessUnitStart(builder)


def ProcessUnitAddOptionsType(builder, optionsType):
    builder.PrependUint8Slot(0, optionsType, 0)


def AddOptionsType(builder, optionsType):
    return ProcessUnitAddOptionsType(builder, optionsType)


def ProcessUnitAddOptions(builder, options):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(options), 0
    )


def AddOptions(builder, options):
    return ProcessUnitAddOptions(builder, options)


def ProcessUnitEnd(builder):
    return builder.EndObject()


def End(builder):
    return ProcessUnitEnd(builder)


import tflite.BertTokenizerOptions
import tflite.NormalizationOptions
import tflite.ProcessUnitOptions
import tflite.RegexTokenizerOptions
import tflite.ScoreCalibrationOptions
import tflite.ScoreThresholdingOptions
import tflite.SentencePieceTokenizerOptions

try:
    pass
except:
    pass


class ProcessUnitT(object):

    # ProcessUnitT
    def __init__(self):
        self.optionsType = 0  # type: int
        self.options = (
            None
        )  # type: Union[None, tflite.NormalizationOptions.NormalizationOptionsT, tflite.ScoreCalibrationOptions.ScoreCalibrationOptionsT, tflite.ScoreThresholdingOptions.ScoreThresholdingOptionsT, tflite.BertTokenizerOptions.BertTokenizerOptionsT, tflite.SentencePieceTokenizerOptions.SentencePieceTokenizerOptionsT, tflite.RegexTokenizerOptions.RegexTokenizerOptionsT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        processUnit = ProcessUnit()
        processUnit.Init(buf, pos)
        return cls.InitFromObj(processUnit)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, processUnit):
        x = ProcessUnitT()
        x._UnPack(processUnit)
        return x

    # ProcessUnitT
    def _UnPack(self, processUnit):
        if processUnit is None:
            return
        self.optionsType = processUnit.OptionsType()
        self.options = tflite.ProcessUnitOptions.ProcessUnitOptionsCreator(
            self.optionsType, processUnit.Options()
        )

    # ProcessUnitT
    def Pack(self, builder):
        if self.options is not None:
            options = self.options.Pack(builder)
        ProcessUnitStart(builder)
        ProcessUnitAddOptionsType(builder, self.optionsType)
        if self.options is not None:
            ProcessUnitAddOptions(builder, options)
        processUnit = ProcessUnitEnd(builder)
        return processUnit