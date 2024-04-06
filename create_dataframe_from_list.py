from __future__ import annotations
import pandas as pd
'''
problem description:
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.
'''

def create_DataFrame(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(data=student_data, columns=['student_id', 'age'])

if __name__ == '__main__':
    student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]
    ret = create_DataFrame(student_data=student_data)
    print(ret)
