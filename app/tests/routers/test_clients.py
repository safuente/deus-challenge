from fastapi.testclient import TestClient


class TestCargo:
    """
    Test suite for the Cargo API endpoints.
    This class contains tests for creating, retrieving, listing, updating, and deleting cargo records.
    """

    def test_create_cargo_with_invalid_contract(self, client: TestClient) -> None:
        """
        Attempting to create a cargo with a non-existent contract_id should fail.
        """
        response = client.post(
            "/cargoes/",
            json={
                "description": "Electronics",
                "weight": 500.5,
                "volume": 10.0,
                "contract_id": 999,
                "status": "pending",
            },
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Contract ID 999 does not exist"

    def test_create_cargo_with_valid_contract(self, client: TestClient) -> None:
        """
        Cargo should only be created if the contract_id exists.
        """
        # Create a valid client
        client_response = client.post(
            "/clients/", json={"name": "John Doe", "contact_info": "john@example.com"}
        )
        assert (
            client_response.status_code == 200
        ), client_response.text  # Debugging output
        client_id = client_response.json()["client_id"]

        # Create a valid contract first
        contract_response = client.post(
            "/contracts/",
            json={
                "client_id": client_id,
                "destination": "New York",
                "price": 1000.0,
                "status": "active",
            },
        )
        assert contract_response.status_code == 200
        contract_id = contract_response.json()["contract_id"]

        # Create a cargo associated with the contract
        cargo_response = client.post(
            "/cargoes/",
            json={
                "description": "Electronics",
                "weight": 500.5,
                "volume": 10.0,
                "contract_id": contract_id,
                "status": "pending",
            },
        )
        assert cargo_response.status_code == 200
        assert "cargo_id" in cargo_response.json()

    def test_get_cargo(self, client: TestClient) -> None:
        """
        Retrieve a cargo by its ID. The response should be either 200 (found) or 404 (not found).
        """
        response = client.get("/cargoes/1")
        assert response.status_code in [200, 404]

    def test_list_cargoes(self, client: TestClient) -> None:
        """
        List all cargo records. The response should return status code 200.
        """
        response = client.get("/cargoes/")
        assert response.status_code == 200

    def test_update_cargo(self, client: TestClient) -> None:
        """
        Update a cargo status. The response should be either 200 (successful) or 404 (not found).
        """
        response = client.put("/cargoes/1", json={"status": "shipped"})
        assert response.status_code in [200, 404]

    def test_delete_cargo(self, client: TestClient) -> None:
        """
        Delete a cargo by its ID. The response should be either 200 (successful) or 404 (not found).
        """
        response = client.delete("/cargoes/1")
        assert response.status_code in [200, 404]


class TestClients:
    """
    Test suite for the Client API endpoints.
    This class contains tests for creating, retrieving, listing, updating, and deleting client records.
    """

    def test_create_client(self, client: TestClient) -> None:
        """
        Create a new client and verify the response contains a valid client ID.
        """
        response = client.post(
            "/clients/", json={"name": "John Doe", "contact_info": "john@example.com"}
        )
        assert response.status_code == 200
        assert "client_id" in response.json()

    def test_get_client(self, client: TestClient) -> None:
        """
        Retrieve a client by its ID.
        """
        response = client.get("/clients/1")
        assert response.status_code == 200

    def test_list_clients(self, client: TestClient) -> None:
        """
        List all client records.
        """
        response = client.get("/clients/")
        assert response.status_code == 200

    def test_update_client(self, client: TestClient) -> None:
        """
        Update a client’s information and verify the response contains the updated details.
        """
        response = client.put(
            "/clients/1", json={"name": "Jane Doe", "contact_info": "st unknown 2"}
        )
        assert "st unknown 2" in response.text
        assert response.status_code == 200

    def test_prevent_delete_client_with_active_contract(
        self, client: TestClient
    ) -> None:
        """
        Attempt to delete a client with an active contract should return a 400 status code.
        """
        response = client.delete("/clients/1")
        assert response.status_code == 400

    def test_delete_client(self, client: TestClient) -> None:
        """
        Create and delete a client, verifying a successful deletion with a 200 status code.
        """
        client_response = client.post(
            "/clients/", json={"name": "John Doe", "contact_info": "john@example.com"}
        )
        client_id = client_response.json()["client_id"]
        response = client.delete(f"/clients/{client_id}")
        assert response.status_code == 200
