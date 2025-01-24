"""Tests for the Asteroid Odyssey SDK."""

import pytest
from asteroid_odyssey import AsteroidOdyssey
from asteroid_odyssey.exceptions import SimulationError

def test_initialization():
    """Test that the SDK initializes correctly."""
    odyssey = AsteroidOdyssey()
    assert not odyssey._initialized

def test_run():
    """Test that the run method executes without errors."""
    odyssey = AsteroidOdyssey()
    odyssey.run()
    assert odyssey._initialized

def test_simulation_error():
    """Test that simulation errors are handled correctly."""
    # This test would need to be expanded based on actual error conditions
    odyssey = AsteroidOdyssey()
    odyssey.run()  # Should not raise any exceptions
