# Game Stability Analyzer (GSA)

Detect crashes before they happen.

## What it does
GSA analyzes your game performance metrics and detects instability patterns in real-time.

## Features
- Crash risk scoring (0–100)
- FPS instability detection
- Memory spike detection
- Simple integration

## Example

```python
from gsa import GameStabilityAnalyzer

g = GameStabilityAnalyzer()

g.observe({"fps": 60, "memory": 1000})
g.observe({"fps": 40, "memory": 1800})

print(g.analyze())