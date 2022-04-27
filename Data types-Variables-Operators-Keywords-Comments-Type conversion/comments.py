"""
Author: Vamsi
Team: DevOps
Infra: Docker deployment
Dependency: Python3.7, Boto3
Functionality: Works for the login functionality
Expected input: username & password
"""
# below code will calculate the total price of items bought
items_count = 10
customer_name = 'vamsi'
is_bill_paid = False 
price = 15.05

print('toal bill to be paid: ', items_count * price)


# To get the RDS database credentials from SSM parameter store
def get_db_credentials():
    pass