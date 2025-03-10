DEUS API CHALLENGE
====================================

* An API designed for managing clients, contracts, cargoes, tracking, and vessels in a shipping system using FastAPI
* SQLite database (local file) with alembic to manage migrations
* Black package was used as a code linter
* Docker is needed to run the app (please use Docker Desktop or Rancher Desktop)

## Run local environment

To run the container please execute the following command:

    make up

Once the command is executed go to the following link http://localhost:8000, you are going to be redirected to API docs

## Data Model
The application's data model is designed to manage cargo shipments, client contracts, and vessel tracking. It consists of the following key entities:

* Client: represents the company's clients, storing their contact information and associated contracts.
* Contract: links a client to a cargo shipment. It contains details about the destination, price, and contract status.
* Cargo: describes the cargo being transported, including its weight, volume, and current status. Each cargo is associated with a contract.
* Tracking: allows tracking of the cargo's location and status throughout its journey, linking it to a specific vessel.
* Vessel: represents ships transporting the cargo, storing their capacity and current location.

Key Relationships
* A client can have multiple contracts.
* Each contract is linked to a single cargo.
* A cargo can have multiple tracking records.
* Each tracking record is associated with a vessel carrying the cargo.

## Other useful commands

Build docker image

    make build

Stop containers

    make stop

Stop containers

    make stop

Delete containers

    make rm

Run unit tests

    make test

Run black linter:

    make lint