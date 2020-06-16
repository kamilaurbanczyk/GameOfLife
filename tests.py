def test(window):
    for i in range(6, 12):
        window.change_state(i, i, 1)
        print(window.window[i][i])

    for i in range(59, 80):
        window.change_state(i, 16, 1)
        print(window.window[i][16])
        for j in range(34, 37):
            window.change_state(i, j, 1)
            print(window.window[i][j])