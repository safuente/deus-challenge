from typing import Any
from fastapi.testclient import TestClient

class TestVessel:
    def test_create_vessel(self, client: TestClient) -> None:
        """A vessel should be created successfully."""
        response = client.post("/vessels/", json={
            "name": "Ocean Explorer",
            "capacity": 10000.0,
            "current_location": "Port of Rotterdam"
        })
        assert response.status_code == 200
        assert "vessel_id" in response.json()

    def test_get_vessel(self, client: TestClient) -> None:
        """Retrieve a vessel by ID."""
        response = client.get("/vessels/1")
        assert response.status_code == 200

    def test_list_vessels(self, client: TestClient) -> None:
        """List all vessels."""
        response = client.get("/vessels/")
        assert response.status_code == 200

    def test_update_vessel(self, client: TestClient) -> None:
        """Update a vessel's current location."""
        response = client.put("/vessels/1", json={"current_location": "Port of Singapore"})
        assert "Port of Singapore" in response.text
        assert response.status_code == 200

    def test_delete_vessel(self, client: TestClient) -> None:
        """Delete a vessel by ID."""
        response = client.delete("/vessels/1")
        assert response.status_code == 200
