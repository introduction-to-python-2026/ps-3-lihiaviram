def approximate_pi(n_terms):
    app=0
    for x in range(n_terms):
        app+=4*((-1)**x/ (2 * x + 1))
    return app
