# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

class ContentProperties(object):
    NONE = 0
    FeatureProperties = 1
    ImageProperties = 2
    BoundingBoxProperties = 3
    AudioProperties = 4

def ContentPropertiesCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == ContentProperties().FeatureProperties:
        import tflite.FeatureProperties
        return tflite.FeatureProperties.FeaturePropertiesT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == ContentProperties().ImageProperties:
        import tflite.ImageProperties
        return tflite.ImageProperties.ImagePropertiesT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == ContentProperties().BoundingBoxProperties:
        import tflite.BoundingBoxProperties
        return tflite.BoundingBoxProperties.BoundingBoxPropertiesT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == ContentProperties().AudioProperties:
        import tflite.AudioProperties
        return tflite.AudioProperties.AudioPropertiesT.InitFromBuf(table.Bytes, table.Pos)
    return None
