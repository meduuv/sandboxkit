"""Offline sandbox policy metadata helpers."""
def normalize(profile):
    return {k: profile[k] for k in sorted(profile)}
def missing_limits(profile, required=("cpu", "memory", "timeout")):
    return [k for k in required if k not in profile]
def within_limits(profile, limits):
    return all(profile.get(k, 0) <= value for k, value in limits.items())
