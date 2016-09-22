import pytest


def test_get_env_setting_raises():
    from ebmdatalab import bigquery
    with pytest.raises(StandardError):
        bigquery.get_env_setting('FROB1234')


def test_get_env_setting_default():
    from ebmdatalab import bigquery
    result = bigquery.get_env_setting('FROB1234', 'foo')
    assert result == 'foo'
