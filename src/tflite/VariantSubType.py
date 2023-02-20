# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class VariantSubType(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VariantSubType()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVariantSubType(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def VariantSubTypeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed
        )

    # VariantSubType
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VariantSubType
    def Shape(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int32Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4),
            )
        return 0

    # VariantSubType
    def ShapeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # VariantSubType
    def ShapeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # VariantSubType
    def ShapeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # VariantSubType
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # VariantSubType
    def HasRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False


def VariantSubTypeStart(builder):
    builder.StartObject(3)


def Start(builder):
    return VariantSubTypeStart(builder)


def VariantSubTypeAddShape(builder, shape):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(shape), 0)


def AddShape(builder, shape):
    return VariantSubTypeAddShape(builder, shape)


def VariantSubTypeStartShapeVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def StartShapeVector(builder, numElems):
    return VariantSubTypeStartShapeVector(builder, numElems)


def VariantSubTypeAddType(builder, type):
    builder.PrependInt8Slot(1, type, 0)


def AddType(builder, type):
    return VariantSubTypeAddType(builder, type)


def VariantSubTypeAddHasRank(builder, hasRank):
    builder.PrependBoolSlot(2, hasRank, 0)


def AddHasRank(builder, hasRank):
    return VariantSubTypeAddHasRank(builder, hasRank)


def VariantSubTypeEnd(builder):
    return builder.EndObject()


def End(builder):
    return VariantSubTypeEnd(builder)


try:
    pass
except:
    pass


class VariantSubTypeT(object):

    # VariantSubTypeT
    def __init__(self):
        self.shape = None  # type: List[int]
        self.type = 0  # type: int
        self.hasRank = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        variantSubType = VariantSubType()
        variantSubType.Init(buf, pos)
        return cls.InitFromObj(variantSubType)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, variantSubType):
        x = VariantSubTypeT()
        x._UnPack(variantSubType)
        return x

    # VariantSubTypeT
    def _UnPack(self, variantSubType):
        if variantSubType is None:
            return
        if not variantSubType.ShapeIsNone():
            if np is None:
                self.shape = []
                for i in range(variantSubType.ShapeLength()):
                    self.shape.append(variantSubType.Shape(i))
            else:
                self.shape = variantSubType.ShapeAsNumpy()
        self.type = variantSubType.Type()
        self.hasRank = variantSubType.HasRank()

    # VariantSubTypeT
    def Pack(self, builder):
        if self.shape is not None:
            if np is not None and type(self.shape) is np.ndarray:
                shape = builder.CreateNumpyVector(self.shape)
            else:
                VariantSubTypeStartShapeVector(builder, len(self.shape))
                for i in reversed(range(len(self.shape))):
                    builder.PrependInt32(self.shape[i])
                shape = builder.EndVector()
        VariantSubTypeStart(builder)
        if self.shape is not None:
            VariantSubTypeAddShape(builder, shape)
        VariantSubTypeAddType(builder, self.type)
        VariantSubTypeAddHasRank(builder, self.hasRank)
        variantSubType = VariantSubTypeEnd(builder)
        return variantSubType