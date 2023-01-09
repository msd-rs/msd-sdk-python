import pymsd
import google.protobuf as pb
import base64
import datetime
import pandas


def test_easy():
    host = '49.233.31.94:50052'
    #host = '127.0.0.1:50051'
    df = pymsd.msd_query(host, 'select * from kline1d.SH600000 limit 10')
    assert len(df.columns) ==  7
    assert len(df.columns[0].datas) ==  8 * 10


def sh600000_10() -> pymsd.DataFrame:
    data = b'elwKBGRhdGUQgYAYelAAAHJIcDwTDQAAwdkEixMNAAAQa5nZEw0AAP0eV8UUDQAATLDrExUNAACbQYBiFQ0AAOrSFLEVDQAAOWSp/xUNAAAmGGfrFg0AAHWp+zkXDXpcCgRvcGVuEIKAGHpQAAAAAAALhiAAAAAAAArGIAAAAAAACuIgAAAAAAALBCAAAAAAAArkIAAAAAAAClogAAAAAAAKoCAAAAAAAAq+IAAAAAAACoAgAAAAAAAKVSB6XAoEaGlnaBCCgBh6UAAAAAAAC6QgAAAAAAALFiAAAAAAAAsOIAAAAAAACwkgAAAAAAAK7SAAAAAAAAqeIAAAAAAACsYgAAAAAAAKwSAAAAAAAAqHIAAAAAAACl8gelsKA2xvdxCCgBh6UAAAAAAACowgAAAAAAAKwSAAAAAAAArZIAAAAAAACtIgAAAAAAAKWCAAAAAAAApNIAAAAAAACnYgAAAAAAAKeCAAAAAAAApGIAAAAAAACjIgel0KBWNsb3NlEIKAGHpQAAAAAAAK1yAAAAAAAArTIAAAAAAACvUgAAAAAAAK1yAAAAAAAApfIAAAAAAACp4gAAAAAAAKjiAAAAAAAAqAIAAAAAAAClUgAAAAAAAKVSB6XgoGdm9sdW1lEIKAGHpQAAABIaAEAAAAAAAw+FmAAAAAABkg+kAAAAAAE9h04AAAAAAlfGEAAAAAABAIieAAAAAADa8UkAAAAAAIsg+QAAAAAAjEW1AAAAAABgiQMAB6XgoGYW1vdW50EIKAGHpQAAAACmBTiAAAAAABwKkIAAAAAADlAJwAAAAAALXmaAAAAAABYls8AAAAAACZY5QAAAAAAIDiJAAAAAAAUgO0AAAAAABUdqgAAAAAADqnPAA='

    data = base64.b64decode(data)
    df = pymsd.DataFrame()
    df.ParseFromString(data)
    return df

def test_pandas():
    df = sh600000_10()
    df = pymsd.to_pandas_dataframe(df)

    assert len(df.columns) == 6
    assert df.index.name == 'date'

    assert len(df) == 10

    assert df.index[0] == pandas.Timestamp(year=1999, month=11, day=10)
    assert df.index[-1] == pandas.Timestamp(year=1999, month=11, day=23)

def test_polars():
    df = sh600000_10()
    df = pymsd.to_polars_dataframe(df)

    assert len(df.columns) == 7
    assert len(df) == 10

    assert df['date'][0] == datetime.datetime(1999, 11, 10)
    assert df['date'][-1] == datetime.datetime(1999, 11, 23)