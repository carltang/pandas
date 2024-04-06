from __future__ import annotations
import pandas as pd
'''
problem description:
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.

The result format is in the following example.

 

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.
'''

def select_data(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

if __name__ == '__main__':
    student_data = pd.DataFrame(data=[[101, 'Ulysses', 13], \
                    [53, 'William', 10], \
                    [128, 'Henry', 6], \
                    [3, 'Henry', 11]], columns=['student_id', 'name', 'age'])
    ret = select_data(students=student_data)
    print(ret)