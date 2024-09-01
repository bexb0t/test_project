from collections import deque
from typing import Deque


def simplify_path(path: str) -> str:

    # split on /
    dirs = path.split("/")
    print(f"dirs: {dirs}")
    cleaned_paths: Deque[str] = deque([])
    for dir in dirs:
        if dir in ["", "."]:
            continue
        if dir == "..":
            if len(cleaned_paths) > 0:
                # remove the previously appended item
                cleaned_paths.pop()
        else:
            cleaned_paths.append(dir)
    return "/" + "/".join(cleaned_paths)


path = "///"
expected = "/"
# Multiple slashes should be replaced by a single one.
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected

path = "/./././."
expected = "/"
# Single period refers to the current directory and should be ignored.
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected


path = "/home/"
expected = "/home"
# The trailing slash should be removed.
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected


path = "/home//foo/"
expected = "/home/foo"
# Multiple consecutive slashes are replaced by a single one.
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected

path = "/home/user/Documents/../Pictures"
expected = "/home/user/Pictures"
# A double period ".." refers to the directory up a level.
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected


path = "/../"
expected = "/"
# Going one level up from the root directory is not possible.
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected

path = "/.../a/../b/c/../d/./"
expected = "/.../b/d"
# "..." is a valid name for a directory in this problem.
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected

path = "/a/b/c/../../"
expected = "/a"
# The path navigates up two levels, ending in the directory "a".
result = simplify_path(path)
print(f"result: {result}, expected: {expected}")
assert result == expected
