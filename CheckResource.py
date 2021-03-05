import boto3


class CheckResource:
    query = """select * from {0}.{1} where time between ago(10m) and now() limit 1 """
    client = boto3.client('timestream-query')

    def __init__(self, database, table):
        self.database = database
        self.table = table

    def getResults(self):
        try:
            results = CheckResource.client.query(QueryString=CheckResource.query.format(self.database, self.table))
            if len(results['Rows']) == 0:
                return [1, self.database, self.table]
            else:
                return [0, self.database, self.table]
        except:
            return [1, self.database, self.table]




