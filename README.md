# 🏺 L.A.T.H.E. (Learning & Adaptive Tutoring Heuristic Engine)

> **The Cognitive Sculpting System.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## ⚠️ The Problem
Most AI tutors fail because they treat every confusion the same way: with more information.
But often, a student's block isn't a lack of data—it's a rigid mental model, a cognitive bias, or a hidden assumption.

## 🛡️ The Solution
**L.A.T.H.E.** acts as a diagnostic hypervisor. It analyzes *why* the student is stuck and summons a specialized "Faculty Agent" to unblock them.

### The Faculty Archetypes
1.  **[span_7](start_span)The Illuminator:** Builds from the ground up using First Principles (for confusion)[span_7](end_span).
2.  **[span_8](start_span)The Paradox:** Uses koans/contradictions to break rigid logic loops (for frustration)[span_8](end_span).
3.  **[span_9](start_span)The Mirror:** Exposes cognitive illusions and biases (for overconfidence)[span_9](end_span).
4.  **[span_10](start_span)The Deconstructor:** Reveals historical/social constructions (for ideology)[span_10](end_span).

## 🚀 Quick Start
```python
from lathe.headmaster import LatheHeadmaster

tutor = LatheHeadmaster()
response = tutor.session("It's obvious that money has intrinsic value.")
# Output: The Deconstructor challenges the historical construct of value.
