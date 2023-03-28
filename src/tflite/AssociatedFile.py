# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AssociatedFile(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AssociatedFile()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAssociatedFile(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def AssociatedFileBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4D\x30\x30\x31", size_prefixed=size_prefixed)

    # AssociatedFile
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AssociatedFile
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AssociatedFile
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AssociatedFile
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # AssociatedFile
    def Locale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AssociatedFile
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def AssociatedFileStart(builder): builder.StartObject(5)
def Start(builder):
    return AssociatedFileStart(builder)
def AssociatedFileAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return AssociatedFileAddName(builder, name)
def AssociatedFileAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def AddDescription(builder, description):
    return AssociatedFileAddDescription(builder, description)
def AssociatedFileAddType(builder, type): builder.PrependInt8Slot(2, type, 0)
def AddType(builder, type):
    return AssociatedFileAddType(builder, type)
def AssociatedFileAddLocale(builder, locale): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(locale), 0)
def AddLocale(builder, locale):
    return AssociatedFileAddLocale(builder, locale)
def AssociatedFileAddVersion(builder, version): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(version), 0)
def AddVersion(builder, version):
    return AssociatedFileAddVersion(builder, version)
def AssociatedFileEnd(builder): return builder.EndObject()
def End(builder):
    return AssociatedFileEnd(builder)

class AssociatedFileT(object):

    # AssociatedFileT
    def __init__(self):
        self.name = None  # type: str
        self.description = None  # type: str
        self.type = 0  # type: int
        self.locale = None  # type: str
        self.version = None  # type: str

    @classmethod
    def InitFromBuf(cls, buf, pos):
        associatedFile = AssociatedFile()
        associatedFile.Init(buf, pos)
        return cls.InitFromObj(associatedFile)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, associatedFile):
        x = AssociatedFileT()
        x._UnPack(associatedFile)
        return x

    # AssociatedFileT
    def _UnPack(self, associatedFile):
        if associatedFile is None:
            return
        self.name = associatedFile.Name()
        self.description = associatedFile.Description()
        self.type = associatedFile.Type()
        self.locale = associatedFile.Locale()
        self.version = associatedFile.Version()

    # AssociatedFileT
    def Pack(self, builder):
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.description is not None:
            description = builder.CreateString(self.description)
        if self.locale is not None:
            locale = builder.CreateString(self.locale)
        if self.version is not None:
            version = builder.CreateString(self.version)
        AssociatedFileStart(builder)
        if self.name is not None:
            AssociatedFileAddName(builder, name)
        if self.description is not None:
            AssociatedFileAddDescription(builder, description)
        AssociatedFileAddType(builder, self.type)
        if self.locale is not None:
            AssociatedFileAddLocale(builder, locale)
        if self.version is not None:
            AssociatedFileAddVersion(builder, version)
        associatedFile = AssociatedFileEnd(builder)
        return associatedFile
