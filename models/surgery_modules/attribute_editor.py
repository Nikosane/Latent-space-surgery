import numpy as np

class AttributeEditor:
    def __init__(self, attribute_vectors):
        """
        attribute_vectors: dict like {'emotion': vector, 'texture': vector}
        """
        self.attribute_vectors = attribute_vectors

    def apply_edit(self, z, attribute, strength=1.0):
        if attribute not in self.attribute_vectors:
            raise ValueError(f"Unknown attribute: {attribute}")
        direction = self.attribute_vectors[attribute]
        return z + strength * direction

    def list_attributes(self):
        return list(self.attribute_vectors.keys())
