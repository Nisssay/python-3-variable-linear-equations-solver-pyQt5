# this is method cramer's 
# import numpy as np


# def solve_3_eq_cramer(a, b, c, d, e, f, g, h, i):
#     detA = np.linalg.det([[a, b, c], [d, e, f], [g, h, i]])
#     detX = np.linalg.det([[d, b, c], [e, f, h], [g, i, 1]])
#     detY = np.linalg.det([[a, d, c], [b, e, h], [g, h, 1]])
#     detZ = np.linalg.det([[a, b, d], [d, e, f], [g, h, i]])
#     x = detX / detA
#     y = detY / detA
#     z = detZ / detA
#     return x, y, z


# # example usage:
# x, y, z = solve_3_eq_cramer(6, 4, 9, 4, 6, 9, 9, 9, 17)
# print(f"x = {x}, y = {y}, z = {z}")

# this is numpy method

# import numpy as np

# # Define the coefficient matrix A and the constant matrix b
# A = np.array([[6, 4, 9], [4, 6, 9], [9, 9, 17]])
# b = np.array([-1, -1, 1])

# # Solve the system of equations
# x = np.linalg.solve(A, b)

# # Print the solutions
# print("x =", x[0])
# print("y =", x[1])
# print("z =", x[2])


# this app is baset on the problem above
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class LinearEquationSolver(QWidget):
    def __init__(self):
        super().__init__()

        # Create the GUI elements
        self.title_label = QLabel("Linear Equation Solver", self)
        self.equation1_label = QLabel("Equation 1: ", self)
        self.equation2_label = QLabel("Equation 2: ", self)
        self.equation3_label = QLabel("Equation 3: ", self)
        self.x_label = QLabel("x = ", self)
        self.y_label = QLabel("y = ", self)
        self.z_label = QLabel("z = ", self)
        self.equation1_input = QLineEdit(self)
        self.equation2_input = QLineEdit(self)
        self.equation3_input = QLineEdit(self)
        self.solve_button = QPushButton("Solve", self)

        # Position the GUI elements
        self.title_label.move(50, 10)
        self.equation1_label.move(20, 50)
        self.equation2_label.move(20, 80)
        self.equation3_label.move(20, 110)
        self.x_label.move(20, 170)
        self.y_label.move(20, 200)
        self.z_label.move(20, 230)
        self.equation1_input.move(100, 50)
        self.equation2_input.move(100, 80)
        self.equation3_input.move(100, 110)
        self.solve_button.move(100, 140)

        # Connect the button to the solve function
        self.solve_button.clicked.connect(self.solve)

        self.x_label.setMinimumWidth(200)
        self.y_label.setMinimumWidth(200)
        self.z_label.setMinimumWidth(200)

        # Set the window size and show the GUI
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("Linear Equation Solver")
        self.show()

    def solve(self):
        # Parse the input values and create the coefficient matrix A and constant matrix b
        eq1 = self.equation1_input.text()
        eq2 = self.equation2_input.text()
        eq3 = self.equation3_input.text()
        A = []
        b = []
        for eq in [eq1, eq2, eq3]:
            coeff = []
            const = 0
            eq_parts = eq.split()
            sign = 1
            for part in eq_parts:
                num_str = ""
                for char in part:
                    if char.isdigit():
                        num_str += char
                    elif char == '-':
                        sign = -1
                    elif char == '+':
                        sign = 1
                if num_str:
                    num = int(num_str) * sign
                    if len(coeff) < 3:
                        coeff.append(num)
                    else:
                        const = num
                sign = 1
            A.append(coeff)
            b.append(const)
        A = np.array(A).reshape(3, 3)
        b = np.array(b)

        # Solve the system of equations
        x = np.linalg.solve(A, b)
        print(A, b, x)

        # Update the GUI labels with the solutions
        self.x_label.setText("x = " + str("{:.2f}".format(x[0])))
        self.y_label.setText("y = " + str("{:.2f}".format(x[1])))
        self.z_label.setText("z = " + str("{:.2f}".format(x[2])))

        self.x_label.repaint()
        self.y_label.repaint()
        self.z_label.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    solver = LinearEquationSolver()
    sys.exit(app.exec_())
