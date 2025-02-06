# Directory Brute Force

## Description
This is a brute force script to discover hidden directories on a web server. It uses a user-provided wordlist to test directories on the target URL in parallel.

## Features
- Discovers hidden directories on a website.
- Uses a user-provided wordlist.
- Performs parallel HTTP requests using `multiprocessing`.
- Highlights found directories in blue and not found directories in red.

## How to Use
### Requirements
- Python 3.x
- `requests` library

### Installation
1. Clone the repository or download the file:
   ```bash
   git clone https://github.com/your-repository/directory-brute-force.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Execution
Run the script specifying the target URL and a wordlist:
```bash
python brute_force.py -u http://example.com -w wordlist.txt
```

### Parameters
- `-u`, `--url`: Target website URL.
- `-w`, `--wordlist`: Path to the file containing the directory wordlist.

## Usage Example
```bash
python brute_force.py -u http://mywebsite.com -w common_dirs.txt
```

## Note
This script is intended for educational purposes and security testing on systems for which you have permission. Unauthorized use may be illegal.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

