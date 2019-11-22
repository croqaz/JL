from json import loads
try:
    from orjson import loads  # type: ignore
except Exception:
    pass
try:
    from ujson import loads  # type: ignore
except Exception:
    pass


def load(file_name):
    for line in open(file_name):
        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Ignore lines starting with comments
        if line[0] == '#':
            continue

        try:
            item = loads(line)
        except Exception as err:
            if len(line) > 45:
                print(f'ERR loading line "{line[:20]}...{line[-20:]}" from "{file_name}" : {err}')
            else:
                print(f'ERR loading line "{line}" from "{file_name}" : {err}')
            continue

        yield item
