# VegaPy

Request and visualise data from vega core and data nodes.


## Setup

The VegaPy repo uses poetry as the package manager. To setup.

```bash
poetry shell
```

```bash
poetry install --all-extras
```

Then update the network config files with.
```bash
make networks
```

And verify setup by running the tests.

```python
pytest tests
```

## Examples

Once setup try running some of the [example scripts](./examples/README.md).