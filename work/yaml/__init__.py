class YAMLError(Exception):
    pass


def safe_load(text):
    """Minimal flat mapping parser for the validator's simple skill frontmatter."""
    result = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise YAMLError(f"Expected key-value pair: {raw_line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise YAMLError("Empty key")
        if value.startswith(('"', "'")):
            quote = value[0]
            if not value.endswith(quote):
                raise YAMLError(f"Unclosed quote for {key}")
            value = value[1:-1]
        result[key] = value
    return result
