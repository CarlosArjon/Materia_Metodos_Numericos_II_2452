import tools.numeric_method.numeric_method as numeric_method
import math
import pandas as pd
from typing import List


class FixedPoint(numeric_method.NumericMethod):
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

            self.parameters["vector_aux"][0] = (-1) * math.sqrt(
                ((25 - math.pow(self.parameters["vector_iterator"][1] + 1, 2))) / 5
            ) - 1

            self.parameters["vector_aux"][1] = math.exp(
                self.parameters["vector_iterator"][0]
            )

            # ==================Logic Method==================END

            # ==================Error Method==================START

            error_value = self.error_calculation(
                tuple(self.parameters["vector_iterator"]),
                tuple(self.parameters["vector_aux"]),
            )

            lst_errors.append(error_value)

            # ==================Error Method==================END

            (
                self.parameters["vector_iterator"][0],
                self.parameters["vector_iterator"][1],
            ) = (
                self.parameters["vector_aux"][0],
                self.parameters["vector_aux"][1],
            )

            self.parameters["table_output"]["x0"].append(
                self.parameters["vector_iterator"][0]
            )

            self.parameters["table_output"]["x1"].append(
                self.parameters["vector_iterator"][1]
            )

            print("x_0 : ", self.parameters["vector_iterator"][0])
            print("\n")
            print("x_1 : ", self.parameters["vector_iterator"][1])

            if (error_value <= 0.000001) and (error_value != 0.0):
                break

            iteracion_newton = iteracion_newton + 1

        print("\n")

        df_data_punto_fijo = pd.DataFrame(
            {
                "x0": self.parameters["table_output"]["x0"],
                "x1": self.parameters["table_output"]["x1"],
                "error": lst_errors,
            }
        )

        print(df_data_punto_fijo)

    def error_calculation(self, vector_before, vector_after):
        return math.dist(vector_before, vector_after)
