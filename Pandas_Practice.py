import pandas as pd

# Pandas import karo aur version print karo.
version = pd.__version__
print(version)

# 1List se DataFrame banao.
data = list(range(10,20))
aaray1D = pd.Series(data)
print(aaray1D)

# Dictionary se DataFrame banao.
data_dic = {
    'name':['Rohit Kumar',None,'Raj kumar','Mohit']*200,
    'Course':['BCA','B-Tech','MCA','BCA']*200,
    'Dept':['IT','Sales','IT',None]*200,
    'Sales': [150000,650000,450000,30000]*200
}
data = pd.DataFrame(data_dic)
data_dic_two = {
    'name':['Rohit Kumar',None,'Raj kumar','Mohit']*200,
    'Course':['BCA','B-Tech','MCA','BCA']*200,
    'Dept':['IT','Sales','IT',None]*200,
    'Sales': [150000,650000,450000,30000]*200
}
data_two = pd.DataFrame(data_dic_two)

# CSV file read karo.
file = data.to_csv('employees_data.csv',index=0)
read = pd.read_csv('employees_data.csv')
print(read)

# First 5 rows dekho (head).
top_5row = data.head(2)
print(top_5row)

# Last 5 rows dekho (tail).
bottum_5row = data.tail(3)
print(bottum_5row)

# Columns ke naam print karo.
column_nm = data.columns
print(column_nm)

# DataFrame ka shape print karo.
data_shape  = data.shape
print(data_shape)

# Data types check karo
data_type = type(data)
print(data_type)
print(data.dtypes)

# Ek column select karo.
print(data['name'])

# Multiple columns select karo.
print(data[['name','Course']])

# # Naya column add karo.
data['City'] = ['Delhi','Jaipur','UP','Uk']*200
# print(data)

# Column delete karo.
del_co = data.drop('City',axis=1,inplace=True)
print(data)

# Missing values check karo.
print(data.isnull().sum())

# Missing values fill karo.
fill = data.fillna({
    'name':'Shivam Kumar',
    'Dept':'HR'
},inplace=True)
print(data)

# Rows filter karo (Salary > 450000).
sls = data['Sales']>450000
print(data[sls])

# Sorting karo kisi column ke basis par.
sort_data = data.sort_values(by='Sales')
print(sort_data)

# Duplicate rows remove karo.
print(data.duplicated().sum())
dup_re = data.drop_duplicates(inplace=True)
print(data)

# GroupBy use karo (Department wise count).
DeptGroupBy = data.groupby(['Dept','name']).sum('Sales')
print(DeptGroupBy)

# Mean / Sum / Max nikalo.
print('Mean = ',data['Sales'].mean())
print('Sum = ',data['Sales'].sum())
print('Max = ',data['Sales'].max())
print('Median = ',data['Sales'].median())
print('Min = ',data['Sales'].min())

# Table 1: Employees
employees = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104],
    'Name': ['Amit', 'Neha', 'Suresh', 'Priya'],
    'Dept_ID': [1, 2, 1, 4]  # Note: Dept_ID 4 departments table mein nahi hai
})
# Table 2: Departments
departments = pd.DataFrame({
    'Dept_ID': [1, 2, 3],
    'Dept_Name': ['IT', 'HR', 'Marketing']
})
# print("Employees Table:\n", employees)
# print("\nDepartments Table:\n", departments)

# Do DataFrames merge karo (inner join).
merged_data_inner = pd.merge(employees,departments, on='Dept_ID',how='inner')
print(merged_data_inner)

# Do DataFrames merge karo (inner join).
merged_data_left = pd.merge(employees,departments, on='Dept_ID',how='left')
print(merged_data_left)

# Pivot table
DeptByAvg = data.pivot_table(index='name',values='Sales',aggfunc='mean')
print(DeptByAvg)

# Use the Apply Function and find the mean of the specific column
sales_mean = data['Sales'].mean()
print(sales_mean)

# Use the lambda function
data['Bonus'] = data['Sales'].apply(lambda x : x+5000,)
print(data)
data['Status'] = data['Sales'].apply(lambda x : 'High' if x > 450000 else 'Low')
print(data)


