import os

class Illuminator:
    def __init__(self):
        self.name = "The Illuminator"
        self.description = "Explains simply from first principles, preserving wonder."
    
    def teach(self, query):
        # In prod: Load 'prompts/illuminator.md' and call LLM
        return f"[{self.name}]: Let's throw away the textbook definitions. Imagine for a second..."
