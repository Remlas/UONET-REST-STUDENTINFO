# UONET-REST-STUDENTINFO
 Using unofficial Python Vulcan UONET+ API to retrieve some basic informations about student - used, for example, for later verification.
 Quite messy code, but maybe in future it will be "un-spaghettied". It was quickly written and patched on production for small school e-sport tournament.

## Installation

Download and launch app from [Docker Hub](https://hub.docker.com/repository/docker/remlas/uonet-rest-studentinfo/general).

```bash
docker pull remlas/uonet-rest-studentinfo
```

## Launch

```bash
docker run -d -p 5000:5000 remlas/uonet-rest-studentinfo
```

## How to use
POST to app root url like "http://localhost:5000/" (no SSL yet, use on localhost only, sorry!) with JSON data in body:
```json
{
  "token": "GD12A2E",
  "symbol": "gdansk",
  "pin": "123456"
}
```
It will return these informations:
```json
{
    "id": 87654,
    "imie": "Name",
    "drugie_imie": "Second Name",
    "nazwisko": "Last Name",
    "plec": "sex",
    "klasa_id": 4321,
    "klasa_kod": "4a",
    "szkola_id": 96,
    "szkola_nazwa": "Full school name",
    "szkola_skrot": "ZSŁ"
}
```

It should be latest middle school of student. See [main.py](main.py) for some exceptions. Currently doesn't return any special debug info, when cannot register (when for example token/symbol/pin is wrong).

## Thanks to
@kapi2289 - [vulcan-api](https://github.com/kapi2289/vulcan-api)

## License

[AGPLv3](https://www.gnu.org/licenses/agpl-3.0.html)