def edit_result_string(string):
    edited_string = string.replace('True', 'true')
    edited_string = edited_string.replace('False', 'false')
    edited_string = edited_string.replace('None', 'null')
    return edited_string
