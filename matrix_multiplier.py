import numpy as np
import streamlit as st


def validate_multiplication(matrix_a, matrix_b):
    """
    Verifica se a multiplicação das matrizes A e B é possível.
    A multiplicação é possível se o número de colunas de A for igual ao número de linhas de B.

    Parâmetros:
        matrix_a (list[list] | np.ndarray): Matriz A.
        matrix_b (list[list] | np.ndarray): Matriz B.

    Retorna:
        bool: True se a multiplicação for possível, False caso contrário.
    """
    cols_a = len(matrix_a[0]) if matrix_a and matrix_a[0] else 0
    rows_b = len(matrix_b)
    return cols_a == rows_b


def multiply_matrices(matrix_a, matrix_b):
    """
    Multiplica as matrizes A e B se forem compatíveis para multiplicação.

    Parâmetros:
        matrix_a (list[list] | np.ndarray): Matriz A.
        matrix_b (list[list] | np.ndarray): Matriz B.

    Retorna:
        np.ndarray: Resultado da multiplicação de A por B.

    Lança:
        ValueError: Se as dimensões não permitirem a multiplicação.
    """
    cols_a = len(matrix_a[0]) if matrix_a and matrix_a[0] else 0
    rows_b = len(matrix_b)

    if cols_a != rows_b:
        raise ValueError(
            "As matrizes não podem ser multiplicadas: número de colunas de A deve ser igual ao número de linhas de B.")

    return np.dot(np.array(matrix_a), np.array(matrix_b))


def create_matrix(rows: int, cols: int, matrix_id: int):
    """
    Cria uma matriz com entradas do usuário através do Streamlit.

    Parâmetros:
        rows (int): Número de linhas da matriz.
        cols (int): Número de colunas da matriz.
        matrix_id (int): Identificador único da matriz para evitar conflitos nos inputs.

    Retorna:
        list[list]: Matriz preenchida pelo usuário.
    """
    matrix = []
    for i in range(rows):
        row_inputs = st.columns(cols)
        row = [col.number_input("", value=0.0, step=1.0, key=f"matrix_{matrix_id}_{i}_{j}", format="%.2f") for j, col in
               enumerate(row_inputs)]
        matrix.append(row)
    return matrix


st.title("Calculadora de Matrizes")

m1 = st.columns(2)
cols_m1 = m1[0].number_input("Qtd Colunas da Matriz A", min_value=1, value=3, step=1)
rows_m1 = m1[1].number_input("Qtd Linhas da Matriz A", min_value=1, value=3, step=1)

st.markdown("#### Matriz A")
matrix1 = create_matrix(rows_m1, cols_m1, 1)

st.markdown("---")

m2 = st.columns(2)
cols_m2 = m2[0].number_input("Qtd Colunas da Matriz B", min_value=1, value=3, step=1)
rows_m2 = m2[1].number_input("Qtd Linhas da Matriz B", min_value=1, value=3, step=1)

st.markdown("#### Matriz B")
matrix2 = create_matrix(rows_m2, cols_m2, 2)

if st.button("Multiplicar Matrizes"):
    matrix1_res = np.array(matrix1)
    matrix2_res = np.array(matrix2)

    if validate_multiplication(matrix1, matrix2):
        st.success("Multiplicação possível: A x B")
        st.write("#### Matriz A:")
        st.write(matrix1_res)
        st.write("#### Matriz B:")
        st.write(matrix2_res)
        try:
            C = multiply_matrices(matrix1_res, matrix2_res)
            st.write("#### Matriz C:")
            st.write("Resultado da multiplicação de A por B:")
            st.write(C)
        except ValueError as e:
            st.error("Erro:", e)
    else:
        st.error("Multiplicação não é possível: as dimensões não são compatíveis.")
