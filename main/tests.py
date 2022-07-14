import uuid
from cacheback.decorators import cacheback

def example_fn(some_uuid: uuid.UUID):
    return "some-string"

def test_non_serializable_input_breaks():
    fn = cacheback(fetch_on_miss=False)(example_fn)
    args = [[uuid.uuid4()]]

    result = fn(*args)

    assert len(fn.job.cache._cache) == 2

    fn(*args)

    assert len(fn.job.cache._cache) == 2
