![SoIG](.github/header.svg)

# SoIG

The Instagram OSINT Tool gets a range of information from an Instagram account that you normally wouldn't be able to get from just looking at their profile.

## Getting Started

**The information includes**:

- **profile** : Username, Profile Name, URL, Followers, Following, Number of Posts, Bio, Profile Picture URL, Is Business Account , Connected to a FB account , External URL, Joined Recently , Business Category Name, Is private , Is Verified.

- **tags** : most used , and by `-t` all used tags.

- **posts** : accessability caption, location, timestamp, comments disabled, Caption, picture url.

### Prerequisites

- Python 3 or higher.
- Linux OS ex. Ubuntu or Kali Linux.

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/SoIG

# move to the project folder
$ cd SoIG
```

### Creating virtual environment

- Create a virtual environment using virtualenv.

```shell
# creating virtual environment
$ virtualenv venv

# activate virtual environment
$ source venv/bin/activate

# install all dependencies
$ pip install -r requirements.txt
```

### Running the Application

- You can run the `main.py` file Manually.

```sh
# Running the Script
$ python3 main.py
```

## Usage

A simple workflow of command used to run SoIG with a Description.

| Usage                                 | Description                                               |
| ------------------------------------- | --------------------------------------------------------- |
| `-h` , `--help`                       | show this help message and exit.                          |
| `-u` USERNAME , `--username` USERNAME | username of account to scan.                              |
| `-p` , `--postscrap`                  | scrape all uploaded images info.                          |
| `-s` , `--savedata`                   | save data to file ( save profile pic, info , post info ). |

## Contributing

- Join the SoIG Creator and Contribute to the Project if you have any enhancement or add-ons to create a good and Secure Project, Help any User to Use it in a good and simple way.

### Disclaimer

- This project can only be used for educational purposes. Using this software against target systems without prior permission is illegal, and any damages from misuse of this software will not be the responsibility of the author.

## License

This project is licensed under the terms of the [MIT license](LICENSE).
