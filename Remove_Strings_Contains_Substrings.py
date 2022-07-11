# Record the algorithm problems I encountered during developing tools at Ford

def remove_dup(list):
    # Check if search strings have the substrings
    if len(list) == 1:
        return list
    if len(list) > 1:
        idx_1, idx_2 = 0, len(list) - 1
        idx_2_times = 0

        """
        eg. search_file_split = ["slog", "slogggger", "slog", "slogg", "fffnvv", "fnv", "fdp"]
        The idx_1 search from the beginning of the search_file_split and idx_2 search from the end of the list
        """
        while idx_1 < idx_2:
            if list[idx_1] in list[idx_2]:
                """
                Check if the string idx_1 is the substring of string idx_2
                If yes, it will remove the string idx_2
                """
                list.remove(list[idx_2])
                idx_2 = len(list) - 1
                idx_2_times = 0
            elif list[idx_2] in list[idx_1]:
                """
                Check if the string idx_2 is the substring of string idx_1
                If yes, it will remove the string idx_1
                """
                list.remove(list[idx_1])
                idx_2 = len(list) - 1
                idx_2_times = 0
            else:
                """
                If there's no matched substrings, idx_2 will move to the next one
                """
                idx_2_times = idx_2_times + 1
                idx_2 = idx_2 - 1

            """
            If finished checking the first string and there's no matched in the following elements
            for example: ["slog", "fnv", "fdppp", "fdp"], since there's no "slog" in ["fnv", "fdppp", "fdp"],
            then idx_1 moves to the next one to check "fnv" based on idx_2_times, 
            if still not found, it moves to "fdppp".
            """
            if idx_2_times == len(list[idx_1:]) - 1:
                idx_1 = idx_1 + 1
                idx_2 = len(list) - 1
                idx_2_times = 0
    return list

if __name__ == '__main__':
    print(remove_dup(list = ["fdp","slogger", "ffnv", "slog", "fnv", "ffdpp", "ffffnvv", "sloggg"]))
    print(remove_dup(list = ["aaabcd", "bcd"]))