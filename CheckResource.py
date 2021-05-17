import boto3


class CheckResource:
    query = """select * from {0}.{1} where time between ago(10m) and now() and tag = '{2}' limit 1 """
    client = boto3.client('timestream-query')

    def __init__(self, database, table, tag):
        self.database = database
        self.table = table
        self.tag = tag

    def getResults(self):
        try:
            results = CheckResource.client.query(QueryString=CheckResource.query.format(self.database, self.table, self.tag))
            if len(results['Rows']) == 0:
                return [1, self.database, self.table]
            else:
                return [0, self.database, self.table]
        except:
            return [1, self.database, self.table]




