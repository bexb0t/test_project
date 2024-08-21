# Bex Ungpiyakul - Senior Software Engineer, API Enablement
# fix to initial approach

from typing import Dict


def count_patterns(text: str) -> Dict[str, int]:
    text = text.lower()
    # print(text)
    matches: Dict[str, int] = {}
    words = text.split(" ")
    for word in words:
        for location, letter in enumerate(word):
            if letter == "i":
                if location < len(word) - 1:
                    pattern = word[location : location + 2]
                else:
                    pattern = word[location]
                if pattern in matches:
                    matches[pattern] += 1
                else:
                    matches[pattern] = 1

    result = dict(sorted(matches.items(), key=lambda item: item[1], reverse=True))

    return result


# input
input = """
I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.
Continuous as the stars that shine
And twinkle on the milky way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.
The waves beside them danced; but they
Out-did the sparkling waves in glee:
A poet could not but be gay,
In such a jocund company:
I gazed—and gazed—but little thought
What wealth the show to me had brought:
For oft, when on my couch I lie
In vacant or in pensive mood,
They flash upon that inward eye
Which is the bliss of solitude;
And then my heart with pleasure fills,
And dances with the daffodils.'
"""

result = count_patterns(input)
print(result)
expected_result = {
    "in": 18,
    "i": 5,
    "il": 5,
    "it": 4,
    "id": 3,
    "ig": 2,
    "is": 2,
    "ic": 1,
    "ie": 1,
    "ir": 1,
    "iv": 1,
}
assert result == expected_result
