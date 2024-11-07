# Passtime.tf
Website made by avery, uploaded here for version control purposes going forward.

## Development Setup

The server requires Flask to run. To install Flask run the following command:
```sh
$ pip install Flask
```
To run the server, simply run `server.py`. This will default to running at `0.0.0.0:5000`.
```
$ python server.py
```
A custom port can be specified by appending another argument like so:
```
$ python server.py 1234
```
Running in debug mode is best for troubleshooting and diagnosing issues.
```
$ python server.py --debug run
```
