"""
To explain the importance of custom modules and for the hands-on
"""

# Note: install boto3 custom module with pip boto3
# There is an advanced concept of requirements.txt we will learn it during the next sessions

import boto3 # custom module by AWS
import util # custom module implemented by us but the in the same folder
from CommonsModule import commons # # custom module implemented by us in the different folder


# boto3 module example for custom modules
def list_s3_buckets():
    print("\n# boto3 module example for custom modules")
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print (bucket.name)

# custom module built by us
def store_invoice_details(name, price, invoice_id):
    print("\n# custom module built by us")
    print("Storing invoice details of the customer; {}, price: {}, invoice_id: {}".format(name, price, invoice_id))
    util.get_db_credentials_param(name='abcd')
    print("Got DB credentials secret")
    print("Establising db connection....")
    print("Storing the details into DB...")
    print("Successfully stored invoice details in the DB!")
    return True

def transfter_amount(account_number, amount):
    print("\n# custom module built by us in a seperate folder")
    print("Transferring the amount: {} to account: {}".format(account_number, amount))
    is_valid_account = commons.check_if_valid_account(account_number=account_number)
    if is_valid_account == True:
        print("Successfully sent the amount: {} to the account: {}".format(amount, account_number))
    else:
        print("Wrong account number!")

# print(boto3)
# list_s3_buckets()
# store_invoice_details(name="Vamsi", price="$150", invoice_id="invoice-12345")
transfter_amount(1234567890, 150)


