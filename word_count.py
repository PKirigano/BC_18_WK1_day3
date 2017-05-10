def word_count(string):
    my_string = string.lower().split()
    my_dict = {}
    for item in my_string:
        my_dict[item] = my_string.count(item)
    print "\n".join(["%s: %s" % (key, ('%('+key+')s') % my_dict) for key in my_dict])