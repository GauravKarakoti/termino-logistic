# Termino-logistic

CLI tool using python to send requests to servers

### How to use

Use the terminal first follow the steps and the `setup.py` file to build this project. Then run the tool by running `termino --help` in the terminal.

```sh
# example with using a yml file
termino -f request.yml
# example with using a json file
termino -f request.json

# use the -c flag for colored response
# example with using a yml file
termino -f -c request.yml
# example with using a json file
termino -f -c request.json
```

### Input Output Redirection

```sh
# the response is written to stdout, and headers/status are written to stderr,
# so that users can take IO redirection to their advantage.
termino -f myrequest.yml > res.json 2> res_headers.txt

# both stdout and stderr can be redirected to the same file
termino -f myrequest.yml > res.txt 2>&1
```

### Sample request file `myrequest.yml`

```yml
# GET Request
url: https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658
method: GET
params:
  offset: 2
  limit: 100
headers:
  accept: text/xml
  accept-language: en
timeout: 5000
```

```yml
# Download a book
url: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
method: GET
```

**By running the command** `termino -f myrequest.yml > book.pdf`.

### A full example file `myrequest.yml`

```yml
method: XXX # (REQUIRED) GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
url: XXX # (REQUIRED) must be prefixed with http:// or https://

params: # url query parameters. have as many as you like
  offset: 0
  limit: 10

data: # data for POST
  name: john
  age: 22
  hobbies:
    - running
    - eating
    - sleeping

data: # you can also type data in json format instead of yaml
  {
    "name": "ash",
    "age": 10,
    "hobbies": ["catching pokemons", "eating", "travelling"]
  }

headers: # have as many as you like
  Content-Type: application/json
  Authorization: <Bearer Token>


cookies: # have as many as you like
  mycookie: <Cookie Value>
  myothercookie: <Other Cookie Value>

timeout: 3.14 # seconds

allow_redirects: true # true or false

proxies: # have as many as you like
  http: http://10.10.1.10:3128
  https: https://10.10.1.11:1080
  ftp: ftp://10.10.1.10:3128

# EITHER verify server's TLS certificate. true or false
verify: true
# OR path to a CA bundle to use
verify: some/folder/cacert.crt

# EITHER path to single ssl client cert file (*.pem)
cert: some/folder/client.pem
# OR (*.cert), (*.key) pair.
cert:
  - some/folder/client.cert
  - some/folder/client.key
```
