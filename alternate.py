#!/usr/bin/env python

"""
Tamper script for sqlmap that applies alternating case strictly to SQL keywords.

Author: YourName
License: MIT
"""

from lib.core.enums import PRIORITY
import re

__priority__ = PRIORITY.HIGH

# List of SQL keywords to target
SQL_KEYWORDS = {
    "ADD",
    "ADD CONSTRAINT",
    "ALL",
    "ALTER",
    "ALTER COLUMN",
    "ALTER TABLE",
    "AND",
    "ANY",
    "AS",
    "ASC",
    "BACKUP DATABASE",
    "BETWEEN",
    "BY",
    "CASE",
    "CHECK",
    "COLUMN",
    "CONSTRAINT",
    "CREATE",
    "CREATE DATABASE",
    "CREATE INDEX",
    "CREATE OR REPLACE VIEW",
    "CREATE PROCEDURE",
    "CREATE TABLE",
    "CREATE UNIQUE INDEX",
    "CREATE VIEW",
    "DATABASE",
    "DEFAULT",
    "DELETE",
    "DESC",
    "DISTINCT",
    "DROP",
    "DROP COLUMN",
    "DROP CONSTRAINT",
    "DROP DATABASE",
    "DROP DEFAULT",
    "DROP INDEX",
    "DROP TABLE",
    "DROP VIEW",
    "ELSE",
    "END",
    "EXISTS",
    "EXEC",
    "FOREIGN KEY",
    "FROM",
    "FULL OUTER JOIN",
    "GROUP",
    "GROUP BY",
    "HAVING",
    "IN",
    "INDEX",
    "INNER",
    "INNER JOIN",
    "INSERT",
    "INSERT INTO",
    "INSERT INTO SELECT",
    "IS",
    "IS NOT NULL",
    "IS NULL",
    "JOIN",
    "LEFT",
    "LEFT JOIN",
    "LIKE",
    "LIMIT",
    "NOT",
    "NOT NULL",
    "NULL",
    "OFFSET",
    "ON",
    "OR",
    "ORDER",
    "ORDER BY",
    "ORD",
    "OUTER",
    "OUTER JOIN",
    "PRIMARY KEY",
    "PROCEDURE",
    "RIGHT",
    "RIGHT JOIN",
    "ROWNUM",
    "SELECT",
    "SELECT DISTINCT",
    "SELECT INTO",
    "SELECT TOP",
    "SET",
    "TABLE",
    "THEN",
    "TOP",
    "TRUNCATE TABLE",
    "UNION",
    "UNION ALL",
    "UNIQUE",
    "UPDATE",
    "VALUES",
    "VIEW",
    "WHEN",
    "WHERE",
}


def dependencies():
    pass


def alternate_case(keyword):
    """Convert a SQL keyword to alternating case, e.g., SELECT -> SeLeCt"""
    return "".join(c.lower() if i % 2 else c.upper() for i, c in enumerate(keyword))


def tamper(payload, **kwargs):
    """
    Applies alternating case to SQL keywords in the given payload.

    Example:
        'SELECT * FROM users WHERE id = 1' → 'SeLeCt * FrOm users WhErE id = 1'
    """

    if not payload:
        return payload

    def replace_keyword(match):
        word = match.group(0).upper()  # Normalize to uppercase for matching
        return alternate_case(word) if word in SQL_KEYWORDS else word

    # Use regex to find whole words that match SQL keywords
    pattern = re.compile(r"\b(?:" + "|".join(SQL_KEYWORDS) + r")\b", re.IGNORECASE)
    tampered_payload = pattern.sub(replace_keyword, payload)

    return tampered_payload
