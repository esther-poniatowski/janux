"""
janux.errors
=============

Exception hierarchy for the Janux package.

All Janux-specific exceptions inherit from :class:`JanuxError`, enabling
callers to catch ``JanuxError`` for broad handling or individual subtypes
for fine-grained control.

Classes
-------
JanuxError
    Base exception for all Janux errors.
ConnectionError
    Raised when an SSH connection cannot be established.
ConfigurationError
    Raised when configuration is invalid or missing.
AuthenticationError
    Raised when authentication with a remote host fails.
"""


class JanuxError(Exception):
    """Base exception for all Janux errors."""


class ConnectionError(JanuxError):
    """Raised when an SSH connection cannot be established."""


class ConfigurationError(JanuxError):
    """Raised when configuration is invalid or missing."""


class AuthenticationError(JanuxError):
    """Raised when authentication with a remote host fails."""
