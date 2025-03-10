from fastapi.testclient import TestClient


class TestContract:
    """
    Test suite for the Contract API endpoints.
    This class contains tests for creating, retrieving, listing, updating, and deleting contract records.
    """

    def test_create_contract_with_invalid_client(self, client: TestClient) -> None:
        """
        Attempting to create a contract with a non-existent client_id should fail.
        """
        response = client.post(
            "/contracts/",
            json={
                "client_id": 999,
                "destination": "Madrid",
                "price": 2000.0,
                "status": "active",
            },
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Client ID 999 does not exist"

    def test_create_contract_with_valid_client(self, client: TestClient) -> None:
        """
        A contract should only be created if the client_id exists.
        """
        # Create a valid client first
        client_response = client.post(
            "/clients/", json={"name": "John Doe", "contact_info": "john@example.com"}
        )
        assert client_response.status_code == 200
        client_id = client_response.json()["client_id"]

        # Create a contract associated with the client
        contract_response = client.post(
            "/contracts/",
            json={
                "client_id": client_id,
                "destination": "Madrid",
                "price": 2000.0,
                "status": "active",
            },
        )
        assert contract_response.status_code == 200
        assert "contract_id" in contract_response.json()

    def test_get_contract(self, client: TestClient) -> None:
        """
        Retrieve a contract by its ID.
        """
        response = client.get("/contracts/1")
        assert response.status_code == 200

    def test_list_contracts(self, client: TestClient) -> None:
        """
        List all contract records. The response should return status code 200.
        """
        response = client.get("/contracts/")
        assert response.status_code == 200

    def test_update_contract(self, client: TestClient) -> None:
        """
        Update a contract's status.
        """
        response = client.put("/contracts/1", json={"status": "completed"})
        assert "completed" in response.text
        assert response.status_code == 200

    def test_delete_contract(self, client: TestClient) -> None:
        """
        Delete a contract by its ID.
        """
        response = client.delete("/contracts/1")
        assert response.status_code == 200
