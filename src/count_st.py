def count_st(word):
    pass
    # base case
    if len(word) < 2:
        return 0
    # recursive case
    else:
        if word[:2] == "st":
            return 1 + count_st(word[2:])
        else:
            return count_st(word[1:])


print(count_st("sttstepstool"))
