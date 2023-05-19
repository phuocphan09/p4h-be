def return_compile_info(code):
    try:
        compile(code, "<string>", "exec")
        return {"error_code": 0}
    except SyntaxError as err:
        return {"error_code": 1, "err_class": err.__class__.__name__, "detail": err.msg,
                "line_no": [err.lineno, err.end_lineno], "char_no": [err.offset, err.end_offset], "line_code": err.text}


def trim_tabs(code):
    trimmed_code = code.lstrip()
    count_lspace = len(code) - len(trimmed_code)
    return {"no_space": count_lspace, "trimmed_code": trimmed_code}


def handle_edge_cases(code):
    # input code must be lstrip-ped

    # else:
    if code[:5] == 'else:':
        return code.replace('else:', '')

    # elif:
    if code[:4] == 'elif':
        return code.replace('elif', 'if  ')  # 2 space to make the offset of error match

    # else, do nothing to the code
    return code


def handle_compile_info(code):
    # trim tabs, save the number of trimmed tabs
    trim_info = trim_tabs(code)
    no_space = trim_info["no_space"]
    trimmed_code = trim_info["trimmed_code"]

    # handle edge cases
    handled_code = handle_edge_cases(trimmed_code)

    # get pure compile info
    compile_info = return_compile_info(handled_code)

    # if success, return
    if compile_info["error_code"] == 0:
        return compile_info

    # if error
    # handle edge cases
    # class, def, if, for, while
    if "expected an indented block after" in compile_info["detail"]:
        return {"error_code": 0}

    # change offset info for trimmed_tabs
    old_offset = compile_info["char_no"]
    new_offset = []
    for offset in old_offset:
        new_offset.append(int(offset + no_space))
    compile_info["char_no"] = new_offset

    # return refined errors
    return compile_info
