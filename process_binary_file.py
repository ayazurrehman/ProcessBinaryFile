
# Write content to file
# f = open("my_file.bin", "wb")
# num = 'Hello world, this world is a really beautiful place. A place like home.'
# arr = bytearray(num, 'utf-8')
# f.write(arr)
# f.close()


def get_repeating_substrings(file_content, min_length):
    file_content_length = len(file_content)
    # sub string and index mapping
    repeating_subs = {}
    # cache to keep track of already added substrings to avoid duplicates
    repeating_sub_indeces = set()

    # loop through all the unique substrings starting with largest possible substrings
    current_subs_len = file_content_length - 1
    while current_subs_len >= min_length:
        index = 0
        # cache to keep track of repeating substrings for current length
        sub_cache = {}
        while index + current_subs_len <= file_content_length:
            # check if substring index is duplicate
            if index in repeating_sub_indeces:
                index += 1
                continue

            sub = file_content[index: index + current_subs_len]
            # add/update to cache, substring details
            if sub in sub_cache:
                sub_cache[sub].append(index)
            else:
                sub_cache[sub] = [index]

            index += 1

            # only add repeating index to mapping of repeating substrings
        for sub in sub_cache:
            if len(sub_cache[sub]) > 1:
                repeating_subs[sub] = sub_cache[sub]
                for index in sub_cache[sub]:
                    repeating_sub_indeces.add(index)

        current_subs_len -= 1

    return repeating_subs


def get_repeating_substrings_from_file(file_path, min_length=5):
    # read binary file
    with open(file_path, "rb") as f:
        file_content_byte = f.read()
        file_content = file_content_byte.decode('utf-8')
        repeating_subs = get_repeating_substrings(file_content=file_content,
                                                  min_length=min_length)

        print("=====Example Output for humans:==========")
        for sub in repeating_subs:
            print(
                "{" + f"{', '.join(str(x) for x in repeating_subs[sub])}" + "}: " + f"'{sub}'")

        print("======Output for binary file:============")
        for sub in repeating_subs:
            sub_byte_array = bytearray(sub, "utf-8")
            print(
                "{" + f"{', '.join(str(x) for x in repeating_subs[sub])}" + "}: " + f"{', '.join(str(x) for x in sub_byte_array)}")


get_repeating_substrings_from_file('my_file.bin')
