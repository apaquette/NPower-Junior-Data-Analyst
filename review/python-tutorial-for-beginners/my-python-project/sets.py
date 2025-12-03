"""Playground for set datatype
"""

MONTHS = {"January", "February", "March"}
for month in MONTHS:
    print(month)

MONTHS.add("April")

print(MONTHS)

MONTHS.remove("January")

print(MONTHS)
