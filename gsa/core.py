class GameStabilityAnalyzer:
    def __init__(self):
        self.history = []

    def observe(self, metrics):
        self.history.append(metrics)

        if len(self.history) > 30:
            self.history.pop(0)

    def analyze(self):
        if len(self.history) < 5:
            return {
                "status": "INSUFFICIENT_DATA",
                "message": "Not enough data to analyze"
            }

        fps_values = [x.get("fps", 0) for x in self.history]
        memory_values = [x.get("memory", 0) for x in self.history]

        fps_drop = max(fps_values) - min(fps_values)
        memory_spike = max(memory_values) - min(memory_values)

        score = 0
        reasons = []

        # FPS impact
        if fps_drop > 10:
            score += 20
            reasons.append("FPS fluctuation detected")

        if fps_drop > 25:
            score += 30

        # Memory impact
        if memory_spike > 300:
            score += 25
            reasons.append("Memory usage spike")

        if memory_spike > 700:
            score += 25

        # تحديد الحالة
        if score < 30:
            status = "STABLE"
        elif score < 70:
            status = "WARNING"
        else:
            status = "CRITICAL"

        return {
            "status": status,
            "crash_score": min(score, 100),
            "reasons": reasons,
            "message": self._generate_message(status)
        }

    def _generate_message(self, status):
        if status == "STABLE":
            return "Game is running smoothly"
        elif status == "WARNING":
            return "Potential instability detected"
        else:
            return "High risk of crash detected"