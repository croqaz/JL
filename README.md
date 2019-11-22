# JL - JSON lines

Python library for parsing JSON lines files.

  [![Pypi Version][pypi-image]][pypi-url]
  [![Build Status][build-image]][build-url]
  [![Python ver][python-image]][python-url]


## Usage

```py
import jl

for item in jl.load('folder/some-file.jl'):
    ...
```


## Installation

```sh
$ pip install jl
```


## Similar libraries

* https://github.com/TeamHG-Memex/json-lines - Read JSON lines (jl) files, including gzipped and broken


## License

[MIT](LICENSE) © Cristi Constantin.


[pypi-image]: https://img.shields.io/pypi/v/jl.svg
[pypi-url]: https://pypi.org/project/jl/
[build-image]: https://github.com/croqaz/dot/workflows/Python/badge.svg
[build-url]: https://github.com/croqaz/dot/actions
[python-image]: https://img.shields.io/badge/Python-3.6-blue.svg
[python-url]: https://python.org
