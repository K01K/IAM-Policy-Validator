# IAM Policy Validator

This Python script provides functions to:

**Import JSON data:** The import_JSON function safely imports and parses JSON data from a file. It handles potential errors like the invalid JSON data.

**Validate policy for wildcards:** The check_Validity function examines the parsed JSON data and checks if any 'Statement' in the policy document has a single asterisk (*) within the Resource field. A single asterisk in this context may indicate overly permissive access, so the function returns False if an asterisk is found and True in every other case

**Usage**
**Save the script:** Save the provided Python code as a file named iam.py
**Save your JSON file:** Save your file with JSON data representing the IAM role policy in the same directory as iam.py and CHANGE THE FILENAME VARIABLE VALUE TO THE NAME OF YOU JSON FILE.
**Run the script:** Execute the script using Python e.g. python iam.py

**Example usage**
Running the script will:
Import the JSON data from the file.
Check for wildcards in the Resource field of any Statement.
Display a message indicating whether the policy contains wildcards (potentially risky) or is valid.

**Error Handling**
File not found: If the script cannot locate the specified JSON file it will raise an FileNotFoundError.
Invalid JSON data: If the script encounters issues parsing the JSON data, it will raise a ValueError.


