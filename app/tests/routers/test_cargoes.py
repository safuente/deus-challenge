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
        assert client_response.status_code == 200
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
        Retrieve a cargo by its ID.
        """
        response = client.get("/cargoes/1")
        assert response.status_code == 200

    def test_list_cargoes(self, client: TestClient) -> None:
        """
        List all cargo records.
        """
        response = client.get("/cargoes/")
        assert response.status_code == 200

    def test_update_cargo(self, client: TestClient) -> None:
        """
        Update a cargo status.
        """
        response = client.put("/cargoes/1", json={"status": "shipped"})
        assert "shipped" in response.text
        assert response.status_code == 200

    def test_delete_cargo(self, client: TestClient) -> None:
        """
        Delete a cargo by its ID.
        """
        response = client.delete("/cargoes/1")
        assert response.status_code == 200
