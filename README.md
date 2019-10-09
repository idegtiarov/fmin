## Small package with `fmin` function

### Installation
Create an empty virtual env.
From `fmin` packege dir:
```
pip install .
```

### Usage

```python
import fmin

fmin.fmin(<your list>)
```

### Tests

Add required packages from the `requirements_test.txt`

```bash
pip install -r requirements_test.txt
```

And run tests:

```bash
python tests.test_functions.py
```
