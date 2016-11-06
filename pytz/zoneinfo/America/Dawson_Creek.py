'''tzinfo timezone information for America/Dawson_Creek.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Dawson_Creek(DstTzInfo):
    '''America/Dawson_Creek timezone definition. See datetime.tzinfo for details'''

    zone = 'America/Dawson_Creek'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1918,4,14,10,0,0),
d(1918,10,31,9,0,0),
d(1942,2,9,10,0,0),
d(1945,8,14,23,0,0),
d(1945,9,30,9,0,0),
d(1947,4,27,10,0,0),
d(1947,9,28,9,0,0),
d(1948,4,25,10,0,0),
d(1948,9,26,9,0,0),
d(1949,4,24,10,0,0),
d(1949,9,25,9,0,0),
d(1950,4,30,10,0,0),
d(1950,9,24,9,0,0),
d(1951,4,29,10,0,0),
d(1951,9,30,9,0,0),
d(1952,4,27,10,0,0),
d(1952,9,28,9,0,0),
d(1953,4,26,10,0,0),
d(1953,9,27,9,0,0),
d(1954,4,25,10,0,0),
d(1954,9,26,9,0,0),
d(1955,4,24,10,0,0),
d(1955,9,25,9,0,0),
d(1956,4,29,10,0,0),
d(1956,9,30,9,0,0),
d(1957,4,28,10,0,0),
d(1957,9,29,9,0,0),
d(1958,4,27,10,0,0),
d(1958,9,28,9,0,0),
d(1959,4,26,10,0,0),
d(1959,9,27,9,0,0),
d(1960,4,24,10,0,0),
d(1960,9,25,9,0,0),
d(1961,4,30,10,0,0),
d(1961,9,24,9,0,0),
d(1962,4,29,10,0,0),
d(1962,10,28,9,0,0),
d(1963,4,28,10,0,0),
d(1963,10,27,9,0,0),
d(1964,4,26,10,0,0),
d(1964,10,25,9,0,0),
d(1965,4,25,10,0,0),
d(1965,10,31,9,0,0),
d(1966,4,24,10,0,0),
d(1966,10,30,9,0,0),
d(1967,4,30,10,0,0),
d(1967,10,29,9,0,0),
d(1968,4,28,10,0,0),
d(1968,10,27,9,0,0),
d(1969,4,27,10,0,0),
d(1969,10,26,9,0,0),
d(1970,4,26,10,0,0),
d(1970,10,25,9,0,0),
d(1971,4,25,10,0,0),
d(1971,10,31,9,0,0),
d(1972,4,30,10,0,0),
d(1972,8,30,9,0,0),
        ]

    _transition_info = [
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PWT'),
i(-25200,3600,'PPT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-28800,0,'PST'),
i(-25200,3600,'PDT'),
i(-25200,0,'MST'),
        ]

Dawson_Creek = Dawson_Creek()

