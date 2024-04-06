import pandas as pd

'''
problem description:
DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
Write a solution to display the first 3 rows of this DataFrame.

 

Example 1:

Input:
DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
Output:
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
Explanation: 
Only the first 3 rows are displayed.
'''
def select_first_Rows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

if __name__ == '__main__':
    data = pd.DataFrame(data=[[846, 'Mason', 21, 'Forward', 'RealMadrid'], \
                                [749, 'Riley', 30, 'Winger', 'Barcelona'], \
                                [155, 'Bob', 28, 'Striker', 'ManchesterUnited'], \
                                [583, 'Isabella', 32, 'Goalkeeper', 'Liverpool'], \
                                [388, 'Zachary', 24, 'Midfielder', 'BayernMunich'], \
                                [883, 'Ava', 23, 'Defender', 'Chelsea'], \
                                [355, 'Violet', 18, 'Striker', 'Juventus'], \
                                [247, 'Thomas', 27, 'Striker', 'ParisSaint-Germain'], \
                                [761, 'Jack', 33, 'Midfielder', 'ManchesterCity'], \
                                [642, 'Charlie', 36, 'Center-back', 'Arsenal']], \
                                    columns=['player_id', 'name', 'age', 'position', 'team'])
    print(select_first_Rows(employees=data))