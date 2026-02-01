from hfr0 import ping, HDIDetector

def test_ping():
    assert ping() == "pong"

def test_hdi_no_alarm_on_start():
    det = HDIDetector(window=5)
    assert det.update(1_000) is False  # not enough samples yet
