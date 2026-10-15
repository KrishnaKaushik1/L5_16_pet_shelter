\# Lab 5: Static Code Analysis



\## 1. Objective



The objective of this lab is to analyze and improve the quality, security, and style of the Python program `pet\_shelter.py` using Pylint, Bandit, and Flake8.



\## 2. Tools Used



1\. \*\*Pylint:\*\* Identifies code quality, naming, documentation, and maintainability issues.

2\. \*\*Bandit:\*\* Identifies potential security issues in Python code.

3\. \*\*Flake8:\*\* Checks Python code for style violations and common errors.



\## 3. Issues Identified and Fixes



| No. | Tool | Issue Identified | Fix Applied |

|---|---|---|---|

| 1 | Pylint | Invalid naming convention for `adoption\_count` | Renamed the module-level constant to `ADOPTION\_COUNT`, updating its references. |

| 2 | Pylint | Use of the `global` statement | Refactored the code to avoid global state. |

| 3 | Pylint | Missing function docstrings | Added docstrings to explain the purpose of functions. |

| 4 | Pylint | Non-standard function naming | Updated function names to follow Python's `snake\_case` convention. |

| 5 | Pylint | Mutable default argument | Replaced the mutable default argument with safe initialization. |

| 6 | Bandit | B311: Use of a standard pseudo-random generator for adoption codes | Replaced the standard random generator with Python's `secrets` module. |

| 7 | Flake8 | E722: Bare `except` clause | Replaced bare exception handling with more appropriate exception handling. |



\*Note: Keep only findings that are confirmed in your original reports and fixes that are present in your final code.\*



\## 4. Before-and-After Results



\### Pylint



\- Before: 6.32/10.

\- After: 10.00/10.

\- Result: The final code achieved a perfect Pylint score.



\### Bandit



\- Before: One low-severity B311 finding.

\- After: No issues identified.

\- Result: The final Bandit scan reported zero issues across all severity levels.



\### Flake8



\- Before: Reported an E722 bare-except violation.

\- After: No violations were displayed.

\- Result: The final Flake8 scan completed without displaying any violations.



\## 5. Reflection



This lab demonstrated how static analysis tools can help improve Python code without requiring the program to be executed for every check.



Pylint helped identify naming convention, documentation, and maintainability issues. Bandit identified the use of a standard pseudo-random generator for adoption codes, which was replaced with Python's `secrets` module. Flake8 helped identify a bare exception-handling clause.



After making the corrections, I reran all three tools and obtained a Pylint score of 10.00/10, no Bandit findings, and no Flake8 violations displayed. I also executed the program to verify that it still ran successfully.



I learned that using multiple static analysis tools provides complementary checks for code quality, security, and style. Keeping before-and-after reports also provides evidence of the improvements made.



\## 6. Conclusion



The static analysis process improved the readability, maintainability, and security of the pet shelter program. The final scans achieved a Pylint score of 10.00/10, reported no Bandit issues, and displayed no Flake8 violations.



\## 7. Evidence



The following reports are included in the `reports/` directory:



\- `pylint\_before.txt`

\- `pylint\_after.txt`

\- `bandit\_before.txt`

\- `bandit\_after.txt`

\- `flake8\_before.txt`

\- `flake8\_after.txt`

