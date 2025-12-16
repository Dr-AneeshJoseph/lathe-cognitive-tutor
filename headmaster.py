from .faculty.illuminator import Illuminator
from .faculty.paradox import Paradox
from .faculty.mirror import Mirror
from .faculty.deconstructor import Deconstructor

class LatheHeadmaster:
    def __init__(self):
        self.faculty = {
            "ILLUMINATOR": Illuminator(),
            "PARADOX": Paradox(),
            "MIRROR": Mirror(),
            "DECONSTRUCTOR": Deconstructor()
        }

    def diagnose(self, query: str):
        """
        Simulate the LLM diagnosis step.
        """
        # MOCK LOGIC FOR DEMO
        if "logically" in query.lower(): return "PARADOX"
        if "obviously" in query.lower(): return "MIRROR"
        if "society" in query.lower(): return "DECONSTRUCTOR"
        return "ILLUMINATOR"

    def session(self, user_query: str):
        print(f"\n🎓 STUDENT: {user_query}")
        
        # 1. Diagnose State
        teacher_key = self.diagnose(user_query)
        teacher = self.faculty[teacher_key]
        
        print(f"⚙️  HEADMASTER: Deploying {teacher.name} ({teacher.description})")
        
        # 2. Teach
        return teacher.teach(user_query)
