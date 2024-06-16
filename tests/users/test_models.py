import pytest


# Test user string representation
def test_user_str(base_user):
    """
    Test that the user string representation is correct.
    """
    assert base_user.__str__() == f"{base_user.username}"


# Test user get_short_name method
def test_user_short_name(base_user):
    """
    Test that user models get_short_name
    """
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name


# Test user get_full_name method
def test_user_full_name(base_user):
    """
    Test that user models get_full_name works
    """
    expected_full_name = f"{base_user.first_name} {base_user.last_name}"
    assert (
        base_user.get_full_name() == expected_full_name
    ), "Full name should match first name and last name"


# Test that the email address is normalized for base user
def test_base_user_email_is_normalized(base_user):
    """
    Test that the email address is normalized
    """
    email = "vbm7752@gmail.com"
    assert base_user.email == email.lower()


# Test that the email address is normalized for super user
def test_super_user_email_is_normalized(super_user):
    """
    Test that the email address is normalized
    """
    email = "vbm7752@gmail.com"
    assert super_user.email == email.lower()


# Test that the super user is not staff
def test_super_user_is_not_staff(user_factory):
    """
    Test that the super user is not staff
    """
    with pytest.raises(ValueError) as err:
        user_factory(is_staff=False, is_superuser=True)
    assert "Superuser must have is_staff=True" in str(err.value)


# Test that the super user is not superuser
def test_super_user_is_not_superuser(user_factory):
    """
    Test that the super user is not superuser
    """
    with pytest.raises(ValueError) as err:
        user_factory(is_superuser=False, is_staff=True)
    assert "Superuser must have is_superuser=True" in str(err.value)


# Test that a user cannot be created without an email
def test_create_user_with_no_email(user_factory):
    """
    Test that a user cannot be created without an email
    """
    with pytest.raises(ValueError) as err:
        user_factory(email=None)
    assert "Email is required" in str(err.value)


# Test that a user cannot be created without a username
def test_create_user_with_no_username(user_factory):
    """
    Test that a user cannot be created without a username
    """
    with pytest.raises(ValueError) as err:
        user_factory(username=None)
    assert "Username is required" in str(err.value)


# Test that a user cannot be created without a first name
def test_create_user_with_no_first_name(user_factory):
    """
    Test that a user cannot be created without a first name
    """
    with pytest.raises(ValueError) as err:
        user_factory(first_name=None)
    assert "First name is required" in str(err.value)


# Test that a user cannot be created without a last name
def test_create_user_with_no_last_name(user_factory):
    """
    Test that a user cannot be created without a last name
    """
    with pytest.raises(ValueError) as err:
        user_factory(last_name=None)
    assert "Last name is required" in str(err.value)


# Test that a super user cannot be created without an email
def test_create_superuser_with_no_email(user_factory):
    """
    Test that a super user cannot be created without an email
    """
    with pytest.raises(ValueError) as err:
        user_factory(email=None, is_staff=True, is_superuser=True)
    assert "Email is required" in str(err.value)


# Test that a super user cannot be created without a password
def test_create_superuser_with_no_password(user_factory):
    """
    Test that a super user cannot be created without a password
    """
    with pytest.raises(ValueError) as err:
        user_factory(password=None, is_staff=True, is_superuser=True)
    assert "Password is required" in str(err.value)


# Test that a user cannot be created with an incorrect email
def test_user_email_incorrect(user_factory):
    """
    Test that a user cannot be created with an incorrect email
    """
    with pytest.raises(ValueError) as err:
        user_factory(email="vbm7752")
    assert "Enter a valid email address" in str(err.value)
