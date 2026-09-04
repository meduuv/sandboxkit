from sandboxkit import missing_limits, normalize, within_limits

def test_policy():
    assert normalize({"memory": 2, "cpu": 1}) == {"cpu": 1, "memory": 2}
    assert missing_limits({"cpu": 1}) == ["memory", "timeout"]
    assert within_limits({"cpu": 1, "memory": 2}, {"cpu": 2, "memory": 4})
