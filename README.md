# Game Stability Analyzer (GSA)

Analyze game performance using FPS and memory patterns to detect instability and crashes.

## 🚀 Features
- Detect FPS drops
- Analyze memory usage
- Calculate stability score
- Identify unstable behavior

## 🧠 Example

```python
from gsa.core import GameStabilityAnalyzer

g = GameStabilityAnalyzer()

data = [
    {"fps": 60, "memory": 1000},
    {"fps": 55, "memory": 1200},
    {"fps": 40, "memory": 1500},
]

for d in data:
    g.observe(d)

result = g.analyze()
print(result)
