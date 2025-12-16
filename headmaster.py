from .faculty.illuminator import Illuminator
from .faculty.paradox import Paradox
# ... import others

class LatheHeadmaster:
    def __init__(self):
        self.illuminator = Illuminator()
        self.paradox = Paradox()
        
    def diagnose(self, user_query: str):
        # MOCK LOGIC
        if "logically" in user_query:
            return "PARADOX"
        return "ILLUMINATOR"

    def session(self, user_query: str):
        strategy = self.diagnose(user_query)
        
        if strategy == "PARADOX":
            return self.paradox.teach(user_query)
        elif strategy == "ILLUMINATOR":
            return self.illuminator.teach(user_query)
          
