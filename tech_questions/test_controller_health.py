import pytest
from controller_health import determine_controller_status

@pytest.mark.parametrize(
    ("cpu, mem, expectation"),
    [
        (45, 50, "HEALTHY"),
        (95, 40, "CRITICAL"),
        (40, 95, "CRITICAL"),
        (89, 89, "HEALTHY"),
        (90, 45, "CRITICAL")
    ]
)
def test_summarize_controllers(cpu, mem, expectation):
    assert determine_controller_status(cpu, mem) == expectation