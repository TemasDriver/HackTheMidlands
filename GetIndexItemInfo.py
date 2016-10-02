
from majesticseo_external_rpc.APIService import *
import random

if(__name__ == '__main__'):
    endpoint = 'https://api.majestic.com/api_command'

    app_api_key = '17D2EA76A0B58C5FAB0A455C320E5197'

    items_to_query = 'https://twitter.com/search?q=Trump&src=tyah'
    items = items_to_query.split(', ')

    # create a hash from the resulting array with the key being
    # 'item0 => first item to query, item1 => second item to query' etc
    parameters = {}
    for index, item in enumerate(items):
        parameters['item' + str(index)] = item

    # add the total number of items to the hash with the key being 'items'
    parameters['items'] = len(items)

    parameters['datasource'] = 'fresh'

    api_service = APIService(app_api_key, endpoint)
    response = api_service.execute_command('GetIndexItemInfo', parameters)

    # check the response code
    if(response.is_ok()):

        # print the results table
        results = response.get_table_for_name('Results')

        for row in results.rows:
            item = row['Item']
            print '\n<' + str(item) + '>'
            for key in sorted(row.keys()):
                if('Item' != key):
                    value = row[key]
                    if  (str(key)=="DownloadBacklinksAnalysisResUnitsCost"):
                        print  int(value) + random.randrange(1000, 5000, 2)
