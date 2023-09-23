exceptions = ['jumps', 'the', 'over']
def Title (title, exceptions):
    fix_title = []

    title = title.split()
    for word in title:
        if word not in exceptions:
            fix_title.append(word.capitalize())
        else:
            fix_title.append(word)
    print(' '.join(fix_title))

Title('the quick brown fox jumps over the lazy dog', exceptions)

