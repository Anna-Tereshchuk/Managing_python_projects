from pathlib import Path
import json
import pytest
import mathlib

here = Path(__file__).absolute().parent

def load_cases(file_name):
    path = here / file_name
    with path.open() as fp:
        for line in fp:
            line = line.strip()  # Remove extra spaces or newlines
            if line:  # Skip empty lines
                obj = json.loads(line)
                yield obj['value'], obj['out'], obj['error']


@pytest.mark.parametrize('value, expected, error', load_cases('sqrt_cases.json'))
def test_sqrt(value, expected, error):
    if error:
        with pytest.raises(ValueError):
            mathlib.sqrt(value)
        return
    out = mathlib.sqrt(value)
    assert expected == round(out, 4), f'sqrt({value}) = {out}, expected {expected}'

