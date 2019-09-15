import urllib.parse


ENV = ''
USER_NAME = ''
PASSWORD = ''
PERIOD = '2019-06-30'

HOST = "http://" + "dummy.restapiexample.com"

PERIOD_WITHOUT_HYPHEN = PERIOD.replace('_','')
FILE_NAME = "output/BATCH_INFO_{0}.json".format(PERIOD)

TOKEN_END_POINT = '/api/auth?login={0}&password={1}'.format(USER_NAME,PASSWORD)
BATCH_SERVICE_END_POINT = '/api/v1/employees'

TOKEN_SERVICE = urllib.parse.urljoin(HOST, TOKEN_END_POINT)
BATCH_SERVICE = urllib.parse.urljoin(HOST, BATCH_SERVICE_END_POINT)
