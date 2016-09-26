import pytest
from mock import patch
from ebmdatalab import bigquery


def test_get_env_setting_raises():
    from ebmdatalab import bigquery
    with pytest.raises(StandardError):
        bigquery.get_env_setting('FROB1234')


def test_get_env_setting_default():
    result = bigquery.get_env_setting('FROB1234', 'foo')
    assert result == 'foo'


def test_get_bq_service():
    import os
    old_env = os.environ.copy()
    if 'GOOGLE_APPLICATION_CREDENTIALS' in old_env:
        del(old_env['GOOGLE_APPLICATION_CREDENTIALS'])
    env = patch.dict('os.environ', old_env, clear=True)
    with env:
        service = bigquery.get_bq_service()
        assert service.projects().list().body is None
