
# CSV Table Display and JSON Extraction Tool

This Python script beautifully formats CSV file contents as a table in the console and allows optional data extraction to a JSON file. Leveraging the `rich` library, it enhances readability and functionality for data manipulation tasks.

## Features

- **Rich Table Display**: Uses the `rich` library to display CSV data in a well-formatted table with customizable text and line colors.
- **JSON Data Extraction**: Optional extraction of CSV data into a JSON file, allowing for easy data reuse and storage.
- **Customizable Display Options**: Includes command-line flags to adjust visual aspects of the table, such as line drawing and text color.

## Requirements

- Python 3.x
- `rich` library

  Install the required library using pip:

  ```bash
  pip install rich
  ```

## Usage

To run the script, navigate to the script's directory and use the following command syntax:

```bash
python 2magic.py [path_to_csv] [options]
```

### Options

- `--verbose`: Prints detailed information about the settings applied during the script's execution.
- `--no-lines`: Disables the drawing of lines in the table.
- `--color [COLOR]`: Sets the text color for the table data. Supported colors are based on the `rich` library documentation.
- `--line-color [COLOR]`: Sets the color for the table lines.
- `--extract [path_to_json]`: Specifies the path to output the JSON file containing the extracted data.

## Examples

Here are some command line examples to get you started:

- Display a CSV file with default settings:

  ```bash
  python 2magic.py data/sample.csv
  ```

- Display a CSV file without line drawings and extract data to a JSON file:

  ```bash
  python 2magic.py data/sample.csv --no-lines --extract data/output.json
  ```

- Display a CSV file with green text and blue lines:

  ```bash
  python 2magic.py data/sample.csv --color green --line-color blue
  ```

## Contributions

Contributions are welcome! If you'd like to improve the script or add features, please fork the repository and submit a pull request.

## License

This script is released under the MIT License. See the LICENSE file for more details.
