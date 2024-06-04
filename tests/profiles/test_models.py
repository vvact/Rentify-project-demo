import pytest

def test_profile_str(profile):
    """Test the profile model string representation"""
    expected_str = f"{profile.user.username}'s Profile"
    assert str(profile) == expected_str
