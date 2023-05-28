import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector and Matrix Calculator")
        self.setGeometry(100, 100, 400, 300)

        self.input_vector1 = QLineEdit(self)
        self.input_vector2 = QLineEdit(self)
        self.input_matrix1 = QLineEdit(self)
        self.input_matrix2 = QLineEdit(self)
        self.result_label = QLabel(self)

        vector_operations_layout = QVBoxLayout()
        vector_operations_layout.addWidget(QLabel("Vector Operations:"))
        vector_operations_layout.addWidget(QLabel("Vector 1:"))
        vector_operations_layout.addWidget(self.input_vector1)
        vector_operations_layout.addWidget(QLabel("Vector 2:"))
        vector_operations_layout.addWidget(self.input_vector2)

        vector_operations_layout.addWidget(QLabel("Matrix Operations:"))
        vector_operations_layout.addWidget(QLabel("Matrix 1:"))
        vector_operations_layout.addWidget(self.input_matrix1)
        vector_operations_layout.addWidget(QLabel("Matrix 2:"))
        vector_operations_layout.addWidget(self.input_matrix2)

        operation_buttons_layout = QHBoxLayout()
        add_button = QPushButton("Add", self)
        add_button.clicked.connect(self.add_vectors)
        operation_buttons_layout.addWidget(add_button)

        subtract_button = QPushButton("Subtract", self)
        subtract_button.clicked.connect(self.subtract_vectors)
        operation_buttons_layout.addWidget(subtract_button)

        multiply_button = QPushButton("Multiply", self)
        multiply_button.clicked.connect(self.multiply_vectors)
        operation_buttons_layout.addWidget(multiply_button)

        vector_product_button = QPushButton("Vector Product", self)
        vector_product_button.clicked.connect(self.vector_product)
        operation_buttons_layout.addWidget(vector_product_button)

        inverse_button = QPushButton("Inverse", self)
        inverse_button.clicked.connect(self.inverse_matrix)
        operation_buttons_layout.addWidget(inverse_button)

        scalar_multiply_button = QPushButton("Scalar Multiply", self)
        scalar_multiply_button.clicked.connect(self.scalar_multiply)
        operation_buttons_layout.addWidget(scalar_multiply_button)

        determinant_button = QPushButton("Determinant", self)
        determinant_button.clicked.connect(self.calculate_determinant)
        operation_buttons_layout.addWidget(determinant_button)

        transpose_button = QPushButton("Transpose", self)
        transpose_button.clicked.connect(self.transpose_matrix)
        operation_buttons_layout.addWidget(transpose_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(vector_operations_layout)
        main_layout.addLayout(operation_buttons_layout)
        main_layout.addWidget(self.result_label)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def get_vector1(self):
        vector_str = self.input_vector1.text()
        vector = list(map(float, vector_str.split(',')))
        return vector

    def get_vector2(self):
        vector_str = self.input_vector2.text()
        vector = list(map(float, vector_str.split(',')))
        return vector

    def get_matrix1(self):
        matrix_str = self.input_matrix1.toPlainText()
        rows = matrix_str.split('\n')
        matrix = [list(map(float, row.split(','))) for row in rows]
        return matrix

    def get_matrix2(self):
        matrix_str = self.input_matrix2.toPlainText()
        rows = matrix_str.split('\n')
        matrix = [list(map(float, row.split(','))) for row in rows]
        return matrix

    def add_vectors(self):
        vector1 = self.get_vector1()
        vector2 = self.get_vector2()
        result = [x + y for x, y in zip(vector1, vector2)]
        self.result_label.setText("Result: " + str(result))

    def subtract_vectors(self):
        vector1 = self.get_vector1()
        vector2 = self.get_vector2()
        result = [x - y for x, y in zip(vector1, vector2)]
        self.result_label.setText("Result: " + str(result))

    def multiply_vectors(self):
        vector1 = self.get_vector1()
        vector2 = self.get_vector2()
        result = sum([x * y for x, y in zip(vector1, vector2)])
        self.result_label.setText("Result: " + str(result))

    def vector_product(self):
        vector1 = self.get_vector1()
        vector2 = self.get_vector2()
        if len(vector1) == 3 and len(vector2) == 3:
            result = [
                vector1[1] * vector2[2] - vector1[2] * vector2[1],
                vector1[2] * vector2[0] - vector1[0] * vector2[2],
                vector1[0] * vector2[1] - vector1[1] * vector2[0]
            ]
            self.result_label.setText("Result: " + str(result))
        else:
            self.result_label.setText("Error: Vector product is only defined for 3D vectors.")

    def inverse_matrix(self):
        matrix = self.get_matrix1()
        # Perform matrix inversion
        # Implement your own logic here
        self.result_label.setText("Result: Inverse matrix")

    def scalar_multiply(self):
        scalar = self.get_vector1()[0]  # Assuming scalar is entered as the first element of the vector
        matrix = self.get_matrix1()
        result = [[scalar * element for element in row] for row in matrix]
        self.result_label.setText("Result: " + str(result))

    def calculate_determinant(self):
        matrix = self.get_matrix1()
        # Perform determinant calculation
        # Implement your own logic here
        self.result_label.setText("Result: Determinant")

    def transpose_matrix(self):
        matrix = self.get_matrix1()
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        self.result_label.setText("Result: " + str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())
