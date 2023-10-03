def Qualitative():
    """
    Color-blind safe qualitiative palette via
    `Paul Tol <https://personal.sron.nl/~pault/>`_.
    """
    colors = [
        '#332288',
        '#88CCEE',
        '#44AA99',
        '#117733',
        '#999933',
        '#DDCC77',
        '#CC6677',
        '#882255',
        '#AA4499',
        '#661100',
        '#6699CC',
        '#AA4466',
        '#4477AA'
    ]

    i = 0

    while i < len(colors):
        yield colors[i]

        i += 1
