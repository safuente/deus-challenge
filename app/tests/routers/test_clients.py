from fastapi.testclient import TestClient


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
