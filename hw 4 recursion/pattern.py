def match_pattern(string, pattern, s_index=0, p_index=0, groups=None):
    # create an empty list for groups if none is provided
    if groups is None:
        groups = []
    # base case: if both string and pattern are empty, return True
    if s_index == len(string) and p_index == len(pattern):
        for i, group in enumerate(groups):
            print(f"{pattern[i]}: {group}")
        return True
    # if either string or pattern is empty, return False
    if s_index == len(string) or p_index == len(pattern):
        return False
    # check if the current character in the string matches the current group in the pattern
    group_len = len(groups[-1]) if groups else 0
    if group_len == 0 or string[s_index:s_index+group_len] == groups[-1]:
        if match_pattern(string, pattern, s_index+group_len, p_index+1, groups):
            return True
    # add the current character to a new group in the pattern
    new_group = string[s_index]
    if new_group not in groups:
        groups.append(new_group)
        if match_pattern(string, pattern, s_index+1, p_index+1, groups):
            return True
        groups.pop()
    # if neither option worked, return False
    return False

string = "codesleepcode"
pattern = "XYX"
if match_pattern(string, pattern):
    pass  # The groups have been printed already in the function
else:
    print("No match found.")




