#!/usr/bin/python3
def text_indentation(text):
    form_text = ""
    lines = []
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        raise ValueError("text is empty")
    for tex in text:
        if tex == ' ' and not form_text:
            continue
        form_text += tex
        if tex in ('.', '?', ':'):
            lines.append(form_text)
            form_text = ""
    lines.append(form_text)
    for i in range(len(lines)-1):
            print(lines[i], end="")
            print()
            print()
    print(lines[-1], end="")
