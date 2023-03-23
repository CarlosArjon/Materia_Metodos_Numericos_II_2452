import tools.numeric_method.numeric_method as numeric_method
import numpy as np
import pandas as pd
import math
from typing import List


class Newton(numeric_method.NumericMethod):
    def __init__(self, parameters: dict) -> None:

        super().__init__(parameters)

    def parameter_validation(self) -> None:
        pass

    def logic_numeric_method(self):

        lst_errors: List[str:float] = []
        iteracion_newton = 0

        while True:

            # ==================Logic Method==================START

            print(
                f"\n===================Iteración {iteracion_newton}===================\n"
            )

            Jacobiana = np.matrix(
                [
                    [
                        10 * math.pow(self.parameters["vector_iterator"][0] + 1, 2),
                        2 * math.pow(self.parameters["vector_iterator"][1] + 1, 2),
                    ],
                    [(-1) * math.exp(self.parameters["vector_iterator"][0]), 1],
                ]
            )

            print("Jacobiana : ", Jacobiana)
            print("\n")

            print("Determinante jacobiana : ", np.linalg.det(Jacobiana))
            print("\n")

            Funcion = np.matrix(
                [
                    [
                        (5 * math.pow(self.parameters["vector_iterator"][0] + 1, 2))
                        + math.pow(self.parameters["vector_iterator"][1] + 1, 2)
                        - 25
                    ],
                    [
                        self.parameters["vector_iterator"][1]
                        - math.exp(self.parameters["vector_iterator"][0])
                    ],
                ]
            )

            Funcion = -1 * Funcion

            print("Funcion : ", Funcion)
            print("\n")

            y = (Jacobiana**-1) * Funcion

            self.parameters["vector_solution"] = (
                np.matrix(
                    [
                        [self.parameters["vector_iterator"][0]],
                        [self.parameters["vector_iterator"][1]],
                    ]
                )
                + y
            )

            print("x_k : ", self.parameters["vector_iterator"])
            print("\n")

            print("y : ", y)
            print("\n")

            print("x_k+1 : x_k + y ", self.parameters["vector_solution"])

            # ==================Logic Method==================END

            # ==================Error Method==================START

            self.parameters["vector_aux"] = [
                self.parameters["vector_solution"].tolist()[0][0],
                self.parameters["vector_solution"].tolist()[1][0],
            ]

            error_value = self.error_calculation(
                tuple(self.parameters["vector_iterator"]),
                tuple(self.parameters["vector_aux"]),
            )

            lst_errors.append(error_value)

            # ==================Error Method==================END

            self.parameters["vector_iterator"] = [
                self.parameters["vector_aux"][0],
                self.parameters["vector_aux"][1],
            ]

            self.parameters["table_output"]["x0"].append(
                self.parameters["vector_iterator"][0]
            )

            self.parameters["table_output"]["x1"].append(
                self.parameters["vector_iterator"][1]
            )

            if (error_value <= 0.000001) and (error_value != 0.0):
                break

            iteracion_newton = iteracion_newton + 1

        df_data_newton = pd.DataFrame(
            {
                "x0": self.parameters["table_output"]["x0"],
                "x1": self.parameters["table_output"]["x1"],
                "error": lst_errors,
            }
        )
        print("\n")
        print(df_data_newton)

    def error_calculation(self, vector_before, vector_after):
        return math.dist(vector_before, vector_after)
