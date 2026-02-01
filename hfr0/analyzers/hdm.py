"""
Hallucination-Drift Index (HDI) detector — MVP placeholder.
Replace with full μ-timing logic as you iterate.
"""
import statistics
from collections import deque

class HDIDetector:
    """Sliding-window z-score detector."""
    def __init__(self, window=50, tau=3.0):
        self.window, self.tau = window, tau
        self.deltas = deque(maxlen=window)

    def update(self, delta_ns: int) -> bool:
        """Return True if drift alarm should fire."""
        self.deltas.append(delta_ns)
        if len(self.deltas) < 10:
            return False
        mu = statistics.mean(self.deltas)
        sigma = statistics.stdev(self.deltas) or 1
        hdi = sum(abs(d - mu) / sigma for d in self.deltas) / len(self.deltas)
        return hdi > self.tau
