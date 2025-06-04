import numpy as np

class MemoryEditor:
    def __init__(self, memory_embeddings):
        """
        memory_embeddings: dict like {'scene1': embedding_vector, 'scene2': ...}
        """
        self.memory_embeddings = memory_embeddings

    def inject_memory(self, z, memory_key, intensity=1.0):
        if memory_key not in self.memory_embeddings:
            raise ValueError(f"Unknown memory: {memory_key}")
        memory_vector = self.memory_embeddings[memory_key]
        return z + intensity * memory_vector

    def remove_memory(self, z, memory_key, intensity=1.0):
        if memory_key not in self.memory_embeddings:
            raise ValueError(f"Unknown memory: {memory_key}")
        memory_vector = self.memory_embeddings[memory_key]
        return z - intensity * memory_vector

    def list_memories(self):
        return list(self.memory_embeddings.keys())

