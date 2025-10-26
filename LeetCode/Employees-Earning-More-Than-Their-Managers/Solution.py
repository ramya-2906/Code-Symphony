import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    emp_mngr =employee.merge(right = employee , how ='inner' , left_on = 'managerId', right_on = 'id', suffixes=('_emp','_mngr'))
    emp_mngr =emp_mngr[['name_emp','salary_emp','name_mngr','salary_mngr']]
    result =emp_mngr[emp_mngr['salary_emp']>emp_mngr['salary_mngr']]
    return result[['name_emp']].rename(columns ={'name_emp':'Employee'})