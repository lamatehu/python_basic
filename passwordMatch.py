import re

passwordRule = re.compile(
    r"""
           (?=.*[a-z])
           (?=.*[A-Z])
           (?=.*[0-9])
           ([A-Za-z\d@$!%*?&]{8,}$)
           """,
    re.VERBOSE,
)
stripRule = re.compile(
    r"""^\s+|\s+$""",
    re.VERBOSE,
)
s = "   hello  "
print(stripRule.sub("", s))
