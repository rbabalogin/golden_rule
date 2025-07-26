def compute_golden_rule(font_size: float) -> list[float]:
    gr_list: list[float] = []

    if font_size < 8:
        return gr_list

    golden_rule = round(font_size / 1.1618)
    gr_list.append(golden_rule)

    gr_list.extend(compute_golden_rule(golden_rule))

    return gr_list
