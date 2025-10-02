
import pytest
from presidio_anonymizer.entities.engine import result
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # prepare input values
    text = "My name is Bond."
    start = 11
    end = 15
    # call `sample_run_anonymizer`
    result =  sample_run_anonymizer(text, start, end)
    # check the output of the call
    return result