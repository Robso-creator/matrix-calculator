import numpy as np
import streamlit as st


def create_matrix(rows: int, cols: int, matrix_id: int):
    """
    Cria uma matriz com entradas do usuário utilizando Streamlit.

    Parâmetros:
        rows (int): Número de linhas da matriz.
        cols (int): Número de colunas da matriz.
        matrix_id (int): Identificador único da matriz para evitar conflitos nos inputs.

    Retorna:
        list[list]: Matriz preenchida pelo usuário.
    """
    matrix = []
    for i in range(rows):
        col_inputs = st.columns(cols)
        row = [
            col.number_input("", value=0.0, step=1.0, key=f"matrix_{matrix_id}_{i}_{j}", format="%.2f")
            for j, col in enumerate(col_inputs)
        ]
        matrix.append(row)
    return matrix


def get_lower_upper(matrix):
    """
    Retorna a matriz triangular inferior e a matriz triangular superior da matriz fornecida.

    Parâmetros:
        matrix (list[list] | np.ndarray): A matriz original.

    Retorna:
        tuple: Uma tupla contendo a matriz triangular inferior e a matriz triangular superior (ambas np.ndarray).
    """
    np_matrix = np.array(matrix)
    lower_matrix = np.tril(np_matrix)
    upper_matrix = np.triu(np_matrix)
    return lower_matrix, upper_matrix


st.title("Matriz Triangular")

st.subheader("Valores da Matriz")
matrix_input = create_matrix(3, 3, 1)

if st.button("Processar Matriz"):
    np_matrix = np.array(matrix_input)
    lower_matrix, upper_matrix = get_lower_upper(np_matrix)
    mid = st.columns(3)
    mid[1].write("### Matriz Original:")
    mid[1].write(np_matrix)

    cols = st.columns(2)
    cols[0].write("### Matriz Triangular Inferior:")
    cols[0].write(lower_matrix)

    cols[1].write("### Matriz Triangular Superior:")
    cols[1].write(upper_matrix)
