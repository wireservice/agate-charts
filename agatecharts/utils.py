from decimal import ROUND_CEILING, ROUND_FLOOR


def round_limit(n):
    """
    Round a axis minimum or maximum to a suitable break point.
    """
    magnitude = n.log10().to_integral_exact(rounding=ROUND_FLOOR)
    fraction = (n / (10 ** magnitude))

    limit = fraction.to_integral_exact(rounding=ROUND_CEILING) * (10 ** magnitude)

    # If value fits within a half magnitude, break there
    if (fraction % 1 < 0.5):
        limit -= (10 ** magnitude) / 2

    return limit


def round_limits(x_min, x_max, y_min, y_max):
    """
    Round off a set of axis limits so they have appropriate margins.
    """
    if x_min is not None:
        if x_min < 0:
            x_min = round_limit(x_max)
        else:
            x_min = 0

    if x_max is not None and x_max != 0:
        if x_max > 0:
            x_max = round_limit(x_max)
        else:
            x_max = 0

    if y_min is not None:
        if y_min < 0:
            y_min = round_limit(x_max)
        else:
            y_min = 0

    if y_max is not None:
        if y_max > 0:
            y_max = round_limit(y_max)
        else:
            y_max = 0

    return (x_min, x_max, y_min, y_max)
