# Elarian Python SDK

[![pypi](https://pypi.org/project/elarian)](https://pypi.org/project/elarian)

> The wrapper provides convenient access to the Elarian APIs.

## Documentation

Take a look at the [API docs here](http://docs.elarian.com).


## Install

You can install the package from [pypi](https://pypi.org/project/elarian) by running: 

```bash
$ pip install elarian
```

## Usage


```python
from elarian import Elarian, Customer

elarian = Elarian(api_key="test_api_key", org_id="test_org", app_id="test_app_id")
customer = Customer(client=elarian, number="+254709759881", provider="cellular")
# get customer state
resp = customer.getState()

print(resp)

```

## Development

```bash
$ git clone https://github.com/ElarianLtd/python-sdk.git
$ cd python-sdk
$ python setup.py
```


Run all tests:

update the following params in your .env file then run python -m unittest discover -v

```bash
sandbox = True
api_key = 
app_id = 
product_id = 
messaging_short_code = 
```

## Issues

If you find a bug, please file an issue on [our issue tracker on GitHub](https://github.com/ElarianLtd/javascript-sdk/issues).