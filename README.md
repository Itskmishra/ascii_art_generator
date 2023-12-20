
# ASCII Art Generator
This Python script facilitates the generation of captivating ASCII art from input text. By leveraging a user-friendly approach, the script allows customization of both the text and art style, making it an engaging tool for creating personalized ASCII art.

## Installation
Ensure you have Python installed on your system. Use the following command to install the required library:

```shell
$ pip install art
```
You can copy the script or clone the repository as per preference.

```
$ git clone https://github.com/Itskmishra/ascii_generator
```
## Usage

- You can use `-h` or `--help` to read about the options and more.
```shell
$ genart -h
usage: ASCII Art Generator [-h] -s STRING [-f FONT] [-o OUTPUT]

example: genascii -s/--string Hello World -f/--font black

options:
  -h, --help            show this help message and exit
  -s STRING, --string STRING
                        text
  -f FONT, --font FONT  font you want to use
  -o OUTPUT, --output OUTPUT
                        specify a file to output the result.

Please dont use space between arguments. Thank you for supporting.


```
- Enter the desired text using `-s` or `--string` flag and it will generate a art with random font style.
```bash
$ genart -s HelloWorld
 _____  ___ __  __ _____   _____   ___      _     ___  ___  ___  ___ 
|_   _|| __|\ \/ /|_   _| |_   _| / _ \    /_\   / __|/ __||_ _||_ _|
  | |  | _|  >  <   | |     | |  | (_) |  / _ \ | (__ \__ \ | |  | | 
  |_|  |___|/_/\_\  |_|     |_|   \___/  /_/ \_\ \___||___/|___||___|
                                                                     

 _   _        _  _         _    _               _      _ 
| | | |      | || |       | |  | |             | |    | |
| |_| |  ___ | || |  ___  | |  | |  ___   _ __ | |  __| |
|  _  | / _ \| || | / _ \ | |/\| | / _ \ | '__|| | / _` |
| | | ||  __/| || || (_) |\  /\  /| (_) || |   | || (_| |
\_| |_/ \___||_||_| \___/  \/  \/  \___/ |_|   |_| \__,_|
                                                         


```
- Define the font style using `-f` or `--font`.
```shell
$ genart -s HelloWorld  -f black

 _____  ___ __  __ _____   _____   ___      _     ___  ___  ___  ___ 
|_   _|| __|\ \/ /|_   _| |_   _| / _ \    /_\   / __|/ __||_ _||_ _|
  | |  | _|  >  <   | |     | |  | (_) |  / _ \ | (__ \__ \ | |  | | 
  |_|  |___|/_/\_\  |_|     |_|   \___/  /_/ \_\ \___||___/|___||___|
                                                                     


 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |  _________   | || |   _____      | || |   _____      | || |     ____     | || | _____  _____ | || |     ____     | || |  _______     | || |   _____      | || |  ________    | |
| | |_   ||   _| | || | |_   ___  |  | || |  |_   _|     | || |  |_   _|     | || |   .'    `.   | || ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || |  |_   _|     | || | |_   ___ `.  | |
| |   | |__| |   | || |   | |_  \_|  | || |    | |       | || |    | |       | || |  /  .--.  \  | || |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |    | |       | || |   | |   `. \ | |
| |   |  __  |   | || |   |  _|  _   | || |    | |   _   | || |    | |   _   | || |  | |    | |  | || |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |    | |   _   | || |   | |    | | | |
| |  _| |  | |_  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |__/ |  | || |  \  `--'  /  | || |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |   _| |__/ |  | || |  _| |___.' / | |
| | |____||____| | || | |_________|  | || |  |________|  | || |  |________|  | || |   `.____.'   | || |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || |  |________|  | || | |________.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
  
```
- Define `-o` or `--output` flag to store the output in a file.
```shell
$ genart -s HelloWorld -f italic -o art.txt
$ cat art.txt
/  /  (- (  (  () |/|/  () /  (  (/  
```

- 

### Dependencies
* Python 3.x
* art library (installed via pip)

#### License
This script is open-source and available under the MIT License. Feel free to explore and enhance the script as needed!
