import boto3
ddb = boto3.client("dynamodb")

def handler(event, context):
    year = str(2008);
    try:
        data = ddb.get_item(
            TableName="ChineseYear",
            Key={
                'Year': {
                    'N': year
                }
            }
        )

        print ("Result from DB: ", year, data['Item']['Animal']['S'] )
        return {"message": "Successfully executed"}
    except Exception as e:
        print("Exception = ",e)
        print ("The provided year: {} doesn't exist in db.".format(year))
        return {"message": "Failed at line 21"}
 
    