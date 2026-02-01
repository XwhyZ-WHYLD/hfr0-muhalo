from .analyzers.hdm import HDIDetector

__all__ = ["HDIDetector"]

def ping() -> str:  # keeps the smoke test happy
    return "pong"

