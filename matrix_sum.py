import numpy as np
import streamlit as st


def validate_addition(matrix_a, matrix_b):
    """
    Verifica se a soma das matrizes A e B é possível.
    A soma é possível se as matrizes tiverem o mesmo número de linhas e colunas.

    Parâmetros:
        matrix_a (list[list] | np.ndarray): Matriz A.
        matrix_b (list[list] | np.ndarray): Matriz B.

    Retorna:
        bool: True se a soma for possível, False caso contrário.
    """
    if not matrix_a or not matrix_b:
        return False

    if len(matrix_a) != len(matrix_b):
        return False

    if matrix_a[0] and matrix_b[0]:
        if len(matrix_a[0]) != len(matrix_b[0]):
            return False
    else:
        return False

    return True


def add_matrices(matrix_a, matrix_b):
    """
    Soma as matrizes A e B elemento a elemento.

    Parâmetros:
        matrix_a (list[list] | np.ndarray): Matriz A.
        matrix_b (list[list] | np.ndarray): Matriz B.

    Retorna:
        np.ndarray: Resultado da soma de A e B.

    Lança:
        ValueError: Se as dimensões das matrizes não permitirem a soma.
    """
    if not validate_addition(matrix_a, matrix_b):
        raise ValueError("As matrizes não podem ser somadas: as dimensões devem ser iguais.")
    return np.add(np.array(matrix_a), np.array(matrix_b))


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
        row = [
            col.number_input(
                "",
                value=0.0,
                step=1.0,
                key=f"matrix_{matrix_id}_{i}_{j}",
                format="%.2f"
            )
            for j, col in enumerate(row_inputs)
        ]
        matrix.append(row)
    return matrix


# Interface principal do Streamlit
st.title("Calculadora de Soma de Matrizes")

# Configuração da Matriz A
st.subheader("Configuração Matriz A")
m1 = st.columns(2)
cols_a = m1[0].number_input("Qtd Colunas da Matriz A", min_value=1, value=3, step=1)
rows_a = m1[1].number_input("Qtd Linhas da Matriz A", min_value=1, value=3, step=1)
st.subheader("Matriz A")
matrix_a = create_matrix(rows_a, cols_a, 1)

st.markdown("---")

# Configuração da Matriz B
st.subheader("Configuração Matriz B")

m2 = st.columns(2)
cols_b = m2[0].number_input("Qtd Colunas da Matriz B", min_value=1, value=3, step=1)
rows_b = m2[1].number_input("Qtd Linhas da Matriz B", min_value=1, value=3, step=1)
st.subheader("Matriz B")
matrix_b = create_matrix(rows_b, cols_b, 2)

st.markdown("---")

if st.button("Somar Matrizes"):
    matrix_a_np = np.array(matrix_a)
    matrix_b_np = np.array(matrix_b)

    if validate_addition(matrix_a, matrix_b):
        st.success("Soma possível: A + B")
        st.write("### Matriz A:")
        st.write(matrix_a_np)
        st.write("### Matriz B:")
        st.write(matrix_b_np)
        try:
            result_matrix = add_matrices(matrix_a, matrix_b)
            st.write("### Resultado da soma das matrizes (A + B):")
            st.write(result_matrix)
        except ValueError as e:
            st.error(f"Erro: {e}")
    else:
        st.error("A soma não é possível: as matrizes devem ter as mesmas dimensões.")
