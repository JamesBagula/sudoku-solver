# app.py
from flask import Flask, render_template, request
from solver import solve_sudoku

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    solution = None
    if request.method == 'POST':
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                cell_value = request.form.get(f'cell-{i}-{j}')
                row.append(int(cell_value) if cell_value else 0)
            board.append(row)

        solve_sudoku(board)
        solution = board

    return render_template('index.html', solution=solution)


if __name__ == '__main__':
    app.run(debug=True)
