import re


def is_password_compliant(password):
    """
    Check if a given password meets the organization’s password policy.
    Policy:
    - Minimum length: 12 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character (!@#$%^&*()-_)
    """
    # Define policy constraints
    min_length = 12
    upper_case = r"[A-Z]"
    lower_case = r"[a-z]"
    digit = r"\d"
    special_char = r"[!@#$%^&*()\-_=+]"

    # Check constraints
    if len(password) < min_length:
        return False, "Password must be at least 12 characters long."
    if not re.search(upper_case, password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(lower_case, password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(digit, password):
        return False, "Password must contain at least one digit."
    if not re.search(special_char, password):
        return (
            False,
            "Password must contain at least one special character (!@#$%^&*()-_=+).",
        )

    return True, "Password is compliant."


# Example usage
if __name__ == "__main__":
    test_password = input("Enter a password to check compliance: ")
    compliant, message = is_password_compliant(test_password)
    print(message)
