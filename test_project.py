import pytest
import sys
from project import (
    E_cin_calculator,
    E_pot_calculator,
    check_argv,
    period_calculator,
    theta_t_calculator,
    vel_ang_calculator,
    vel_lin_calculator)

def test_check_argv():
    sys.argv = ["project.py", "10"]
    assert check_argv() == 10.0

    sys.argv = ["project.py"]
    with pytest.raises(SystemExit):
        check_argv()

    sys.argv = ["project.py", "10", "20"]
    with pytest.raises(SystemExit):
        check_argv()

    sys.argv = ["project.py", "-5"]
    with pytest.raises(SystemExit):
        check_argv()

def test_vel_ang_calculator():
    assert round(vel_ang_calculator(30, 9.8, 10, 5), 2) == 0.50
    assert round(vel_ang_calculator(40, 10, 11, 6), 2) != 3.2

def test_vel_lin_calculator():
    assert round(vel_lin_calculator(10, -2.56), 2) == -25.6
    assert round(vel_lin_calculator(12, -4.3), 2) != 33.2

def test_period_calculator():
    assert round(period_calculator(10, 9.8), 2) == 6.35
    assert round(period_calculator(12, 10), 2) != 2.34

def test_E_cin_calculator():
    assert E_cin_calculator(20, 5) == 250
    assert E_cin_calculator(30, 6) != 123

def test_E_pot_calculator():
    assert round(E_pot_calculator(10, 9.8, 10, 30), 2) == 131.3
    assert round(E_pot_calculator(12, 9, 12, 45), 2) != 0.72

def test_theta_t_calculator():
    assert round(theta_t_calculator(30, 9.8, 10, 5), 2) == 7.05
    assert round(theta_t_calculator(12, 10, 23, 4), 2) != 2.21


