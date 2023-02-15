# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SubGraphMetadata(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SubGraphMetadata()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSubGraphMetadata(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def SubGraphMetadataBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4D\x30\x30\x31", size_prefixed=size_prefixed)

    # SubGraphMetadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SubGraphMetadata
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SubGraphMetadata
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SubGraphMetadata
    def InputTensorMetadata(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.TensorMetadata import TensorMetadata
            obj = TensorMetadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SubGraphMetadata
    def InputTensorMetadataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SubGraphMetadata
    def InputTensorMetadataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # SubGraphMetadata
    def OutputTensorMetadata(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.TensorMetadata import TensorMetadata
            obj = TensorMetadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SubGraphMetadata
    def OutputTensorMetadataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SubGraphMetadata
    def OutputTensorMetadataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # SubGraphMetadata
    def AssociatedFiles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.AssociatedFile import AssociatedFile
            obj = AssociatedFile()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SubGraphMetadata
    def AssociatedFilesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SubGraphMetadata
    def AssociatedFilesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # SubGraphMetadata
    def InputProcessUnits(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.ProcessUnit import ProcessUnit
            obj = ProcessUnit()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SubGraphMetadata
    def InputProcessUnitsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SubGraphMetadata
    def InputProcessUnitsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # SubGraphMetadata
    def OutputProcessUnits(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.ProcessUnit import ProcessUnit
            obj = ProcessUnit()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SubGraphMetadata
    def OutputProcessUnitsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SubGraphMetadata
    def OutputProcessUnitsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # SubGraphMetadata
    def InputTensorGroups(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.TensorGroup import TensorGroup
            obj = TensorGroup()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SubGraphMetadata
    def InputTensorGroupsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SubGraphMetadata
    def InputTensorGroupsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # SubGraphMetadata
    def OutputTensorGroups(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.TensorGroup import TensorGroup
            obj = TensorGroup()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SubGraphMetadata
    def OutputTensorGroupsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SubGraphMetadata
    def OutputTensorGroupsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

def SubGraphMetadataStart(builder): builder.StartObject(9)
def Start(builder):
    return SubGraphMetadataStart(builder)
def SubGraphMetadataAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return SubGraphMetadataAddName(builder, name)
def SubGraphMetadataAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def AddDescription(builder, description):
    return SubGraphMetadataAddDescription(builder, description)
def SubGraphMetadataAddInputTensorMetadata(builder, inputTensorMetadata): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(inputTensorMetadata), 0)
def AddInputTensorMetadata(builder, inputTensorMetadata):
    return SubGraphMetadataAddInputTensorMetadata(builder, inputTensorMetadata)
def SubGraphMetadataStartInputTensorMetadataVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartInputTensorMetadataVector(builder, numElems):
    return SubGraphMetadataStartInputTensorMetadataVector(builder, numElems)
def SubGraphMetadataAddOutputTensorMetadata(builder, outputTensorMetadata): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(outputTensorMetadata), 0)
def AddOutputTensorMetadata(builder, outputTensorMetadata):
    return SubGraphMetadataAddOutputTensorMetadata(builder, outputTensorMetadata)
def SubGraphMetadataStartOutputTensorMetadataVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartOutputTensorMetadataVector(builder, numElems):
    return SubGraphMetadataStartOutputTensorMetadataVector(builder, numElems)
def SubGraphMetadataAddAssociatedFiles(builder, associatedFiles): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(associatedFiles), 0)
def AddAssociatedFiles(builder, associatedFiles):
    return SubGraphMetadataAddAssociatedFiles(builder, associatedFiles)
def SubGraphMetadataStartAssociatedFilesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartAssociatedFilesVector(builder, numElems):
    return SubGraphMetadataStartAssociatedFilesVector(builder, numElems)
def SubGraphMetadataAddInputProcessUnits(builder, inputProcessUnits): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(inputProcessUnits), 0)
def AddInputProcessUnits(builder, inputProcessUnits):
    return SubGraphMetadataAddInputProcessUnits(builder, inputProcessUnits)
def SubGraphMetadataStartInputProcessUnitsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartInputProcessUnitsVector(builder, numElems):
    return SubGraphMetadataStartInputProcessUnitsVector(builder, numElems)
def SubGraphMetadataAddOutputProcessUnits(builder, outputProcessUnits): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(outputProcessUnits), 0)
def AddOutputProcessUnits(builder, outputProcessUnits):
    return SubGraphMetadataAddOutputProcessUnits(builder, outputProcessUnits)
def SubGraphMetadataStartOutputProcessUnitsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartOutputProcessUnitsVector(builder, numElems):
    return SubGraphMetadataStartOutputProcessUnitsVector(builder, numElems)
def SubGraphMetadataAddInputTensorGroups(builder, inputTensorGroups): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(inputTensorGroups), 0)
def AddInputTensorGroups(builder, inputTensorGroups):
    return SubGraphMetadataAddInputTensorGroups(builder, inputTensorGroups)
def SubGraphMetadataStartInputTensorGroupsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartInputTensorGroupsVector(builder, numElems):
    return SubGraphMetadataStartInputTensorGroupsVector(builder, numElems)
def SubGraphMetadataAddOutputTensorGroups(builder, outputTensorGroups): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(outputTensorGroups), 0)
def AddOutputTensorGroups(builder, outputTensorGroups):
    return SubGraphMetadataAddOutputTensorGroups(builder, outputTensorGroups)
def SubGraphMetadataStartOutputTensorGroupsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartOutputTensorGroupsVector(builder, numElems):
    return SubGraphMetadataStartOutputTensorGroupsVector(builder, numElems)
def SubGraphMetadataEnd(builder): return builder.EndObject()
def End(builder):
    return SubGraphMetadataEnd(builder)
import tflite.AssociatedFile
import tflite.ProcessUnit
import tflite.TensorGroup
import tflite.TensorMetadata
try:
    from typing import List
except:
    pass

class SubGraphMetadataT(object):

    # SubGraphMetadataT
    def __init__(self):
        self.name = None  # type: str
        self.description = None  # type: str
        self.inputTensorMetadata = None  # type: List[tflite.TensorMetadata.TensorMetadataT]
        self.outputTensorMetadata = None  # type: List[tflite.TensorMetadata.TensorMetadataT]
        self.associatedFiles = None  # type: List[tflite.AssociatedFile.AssociatedFileT]
        self.inputProcessUnits = None  # type: List[tflite.ProcessUnit.ProcessUnitT]
        self.outputProcessUnits = None  # type: List[tflite.ProcessUnit.ProcessUnitT]
        self.inputTensorGroups = None  # type: List[tflite.TensorGroup.TensorGroupT]
        self.outputTensorGroups = None  # type: List[tflite.TensorGroup.TensorGroupT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        subGraphMetadata = SubGraphMetadata()
        subGraphMetadata.Init(buf, pos)
        return cls.InitFromObj(subGraphMetadata)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, subGraphMetadata):
        x = SubGraphMetadataT()
        x._UnPack(subGraphMetadata)
        return x

    # SubGraphMetadataT
    def _UnPack(self, subGraphMetadata):
        if subGraphMetadata is None:
            return
        self.name = subGraphMetadata.Name()
        self.description = subGraphMetadata.Description()
        if not subGraphMetadata.InputTensorMetadataIsNone():
            self.inputTensorMetadata = []
            for i in range(subGraphMetadata.InputTensorMetadataLength()):
                if subGraphMetadata.InputTensorMetadata(i) is None:
                    self.inputTensorMetadata.append(None)
                else:
                    tensorMetadata_ = tflite.TensorMetadata.TensorMetadataT.InitFromObj(subGraphMetadata.InputTensorMetadata(i))
                    self.inputTensorMetadata.append(tensorMetadata_)
        if not subGraphMetadata.OutputTensorMetadataIsNone():
            self.outputTensorMetadata = []
            for i in range(subGraphMetadata.OutputTensorMetadataLength()):
                if subGraphMetadata.OutputTensorMetadata(i) is None:
                    self.outputTensorMetadata.append(None)
                else:
                    tensorMetadata_ = tflite.TensorMetadata.TensorMetadataT.InitFromObj(subGraphMetadata.OutputTensorMetadata(i))
                    self.outputTensorMetadata.append(tensorMetadata_)
        if not subGraphMetadata.AssociatedFilesIsNone():
            self.associatedFiles = []
            for i in range(subGraphMetadata.AssociatedFilesLength()):
                if subGraphMetadata.AssociatedFiles(i) is None:
                    self.associatedFiles.append(None)
                else:
                    associatedFile_ = tflite.AssociatedFile.AssociatedFileT.InitFromObj(subGraphMetadata.AssociatedFiles(i))
                    self.associatedFiles.append(associatedFile_)
        if not subGraphMetadata.InputProcessUnitsIsNone():
            self.inputProcessUnits = []
            for i in range(subGraphMetadata.InputProcessUnitsLength()):
                if subGraphMetadata.InputProcessUnits(i) is None:
                    self.inputProcessUnits.append(None)
                else:
                    processUnit_ = tflite.ProcessUnit.ProcessUnitT.InitFromObj(subGraphMetadata.InputProcessUnits(i))
                    self.inputProcessUnits.append(processUnit_)
        if not subGraphMetadata.OutputProcessUnitsIsNone():
            self.outputProcessUnits = []
            for i in range(subGraphMetadata.OutputProcessUnitsLength()):
                if subGraphMetadata.OutputProcessUnits(i) is None:
                    self.outputProcessUnits.append(None)
                else:
                    processUnit_ = tflite.ProcessUnit.ProcessUnitT.InitFromObj(subGraphMetadata.OutputProcessUnits(i))
                    self.outputProcessUnits.append(processUnit_)
        if not subGraphMetadata.InputTensorGroupsIsNone():
            self.inputTensorGroups = []
            for i in range(subGraphMetadata.InputTensorGroupsLength()):
                if subGraphMetadata.InputTensorGroups(i) is None:
                    self.inputTensorGroups.append(None)
                else:
                    tensorGroup_ = tflite.TensorGroup.TensorGroupT.InitFromObj(subGraphMetadata.InputTensorGroups(i))
                    self.inputTensorGroups.append(tensorGroup_)
        if not subGraphMetadata.OutputTensorGroupsIsNone():
            self.outputTensorGroups = []
            for i in range(subGraphMetadata.OutputTensorGroupsLength()):
                if subGraphMetadata.OutputTensorGroups(i) is None:
                    self.outputTensorGroups.append(None)
                else:
                    tensorGroup_ = tflite.TensorGroup.TensorGroupT.InitFromObj(subGraphMetadata.OutputTensorGroups(i))
                    self.outputTensorGroups.append(tensorGroup_)

    # SubGraphMetadataT
    def Pack(self, builder):
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.description is not None:
            description = builder.CreateString(self.description)
        if self.inputTensorMetadata is not None:
            inputTensorMetadatalist = []
            for i in range(len(self.inputTensorMetadata)):
                inputTensorMetadatalist.append(self.inputTensorMetadata[i].Pack(builder))
            SubGraphMetadataStartInputTensorMetadataVector(builder, len(self.inputTensorMetadata))
            for i in reversed(range(len(self.inputTensorMetadata))):
                builder.PrependUOffsetTRelative(inputTensorMetadatalist[i])
            inputTensorMetadata = builder.EndVector()
        if self.outputTensorMetadata is not None:
            outputTensorMetadatalist = []
            for i in range(len(self.outputTensorMetadata)):
                outputTensorMetadatalist.append(self.outputTensorMetadata[i].Pack(builder))
            SubGraphMetadataStartOutputTensorMetadataVector(builder, len(self.outputTensorMetadata))
            for i in reversed(range(len(self.outputTensorMetadata))):
                builder.PrependUOffsetTRelative(outputTensorMetadatalist[i])
            outputTensorMetadata = builder.EndVector()
        if self.associatedFiles is not None:
            associatedFileslist = []
            for i in range(len(self.associatedFiles)):
                associatedFileslist.append(self.associatedFiles[i].Pack(builder))
            SubGraphMetadataStartAssociatedFilesVector(builder, len(self.associatedFiles))
            for i in reversed(range(len(self.associatedFiles))):
                builder.PrependUOffsetTRelative(associatedFileslist[i])
            associatedFiles = builder.EndVector()
        if self.inputProcessUnits is not None:
            inputProcessUnitslist = []
            for i in range(len(self.inputProcessUnits)):
                inputProcessUnitslist.append(self.inputProcessUnits[i].Pack(builder))
            SubGraphMetadataStartInputProcessUnitsVector(builder, len(self.inputProcessUnits))
            for i in reversed(range(len(self.inputProcessUnits))):
                builder.PrependUOffsetTRelative(inputProcessUnitslist[i])
            inputProcessUnits = builder.EndVector()
        if self.outputProcessUnits is not None:
            outputProcessUnitslist = []
            for i in range(len(self.outputProcessUnits)):
                outputProcessUnitslist.append(self.outputProcessUnits[i].Pack(builder))
            SubGraphMetadataStartOutputProcessUnitsVector(builder, len(self.outputProcessUnits))
            for i in reversed(range(len(self.outputProcessUnits))):
                builder.PrependUOffsetTRelative(outputProcessUnitslist[i])
            outputProcessUnits = builder.EndVector()
        if self.inputTensorGroups is not None:
            inputTensorGroupslist = []
            for i in range(len(self.inputTensorGroups)):
                inputTensorGroupslist.append(self.inputTensorGroups[i].Pack(builder))
            SubGraphMetadataStartInputTensorGroupsVector(builder, len(self.inputTensorGroups))
            for i in reversed(range(len(self.inputTensorGroups))):
                builder.PrependUOffsetTRelative(inputTensorGroupslist[i])
            inputTensorGroups = builder.EndVector()
        if self.outputTensorGroups is not None:
            outputTensorGroupslist = []
            for i in range(len(self.outputTensorGroups)):
                outputTensorGroupslist.append(self.outputTensorGroups[i].Pack(builder))
            SubGraphMetadataStartOutputTensorGroupsVector(builder, len(self.outputTensorGroups))
            for i in reversed(range(len(self.outputTensorGroups))):
                builder.PrependUOffsetTRelative(outputTensorGroupslist[i])
            outputTensorGroups = builder.EndVector()
        SubGraphMetadataStart(builder)
        if self.name is not None:
            SubGraphMetadataAddName(builder, name)
        if self.description is not None:
            SubGraphMetadataAddDescription(builder, description)
        if self.inputTensorMetadata is not None:
            SubGraphMetadataAddInputTensorMetadata(builder, inputTensorMetadata)
        if self.outputTensorMetadata is not None:
            SubGraphMetadataAddOutputTensorMetadata(builder, outputTensorMetadata)
        if self.associatedFiles is not None:
            SubGraphMetadataAddAssociatedFiles(builder, associatedFiles)
        if self.inputProcessUnits is not None:
            SubGraphMetadataAddInputProcessUnits(builder, inputProcessUnits)
        if self.outputProcessUnits is not None:
            SubGraphMetadataAddOutputProcessUnits(builder, outputProcessUnits)
        if self.inputTensorGroups is not None:
            SubGraphMetadataAddInputTensorGroups(builder, inputTensorGroups)
        if self.outputTensorGroups is not None:
            SubGraphMetadataAddOutputTensorGroups(builder, outputTensorGroups)
        subGraphMetadata = SubGraphMetadataEnd(builder)
        return subGraphMetadata
