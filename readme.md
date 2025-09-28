# AAE Decode Utility

This project provides a Python utility to decode Apple's AAE (Adjustment) files, which store photo edit information in XML format. The tool extracts and decodes the `data` block, which is base64-encoded and zlib-compressed, and outputs the decoded data as JSON.

## Features
- Reads AAE XML files
- Decodes and decompresses the `data` block
- Prints decoded data as JSON
- Optionally prints the full XML content with the decoded data

## Usage

```
python3 aae-decode.py <AAE_FILE> [--xml]
```

- `<AAE_FILE>`: Path to the AAE file
- `--xml`: (Optional) Print both the XML content and the decoded `data` block. Without this flag, only the decoded data is printed.

### Examples

Print only decoded data:
```
python3 aae-decode.py example.AAE
```

Print XML and decoded data:
```
python3 aae-decode.py example.AAE --xml
```

## Requirements
- Python 3.x

No external dependencies are required; only the Python standard library is used.

## License
MIT License
