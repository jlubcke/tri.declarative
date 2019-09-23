import pytest
from tri_declarative import with_meta


def test_too_many_args_check():

    @with_meta
    class Test(object):
        class Meta:
            foo = 'foo'

        def __init__(self, foo):
            pass

    with pytest.raises(TypeError) as e:
        Test('foo', 'bar')

    assert 'Too many positional arguments' == str(e.value)


def test_add_init_kwargs():
    @with_meta(add_init_kwargs=True)
    class Test(object):
        class Meta:
            foo = 'bar'
            _bar = 'baz'

        def __init__(self, foo):
            assert 'bar' == foo

    Test()
