PythonEats
==========

Simple client app used to test the
[pact-test](https://github.com/Kalimaha/pact-test) library.

Setup
-----

Build the container through Docker Compose with:

```
docker-compose build app
```

If you want to send generated pact files to the Pact Broker, modify
`.pact.json` file with the correct URL:

```json
{
  "pact_broker_uri": "http://my-pact-broker.com/"
}
```

Pact Test
---------

To run pact tests, simply execute:

```
docker-compose run app
```

This will generate the pact file in `/pacts` folder and upload it to the Pact
Broker.
