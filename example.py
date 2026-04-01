from gsa import GameStabilityAnalyzer

g = GameStabilityAnalyzer()

data = [
    {"fps": 60, "memory": 1000},
    {"fps": 58, "memory": 1100},
    {"fps": 52, "memory": 1200},
    {"fps": 40, "memory": 1600},
    {"fps": 35, "memory": 1800},
]

for d in data:
    g.observe(d)

result = g.analyze()
print("=== Game Stability Report ===")
print(f"Score: {result['stability_score']}")
print(f"Status: {result['status']}")

if result["stability_score"] < 0.5:
    print("⚠️ WARNING: Game instability detected")
