from fastapi.testclient import TestClient


class TestTracking:
    def test_create_tracking_with_invalid_cargo_or_vessel(
        self, client: TestClient
    ) -> None:
        """Trying to create a tracking entry with a non-existent cargo_id or vessel_id should fail."""
        response = client.post(
            "/tracking/",
            json={
                "cargo_id": 999,
                "vessel_id": 999,
                "location": "Port of Hamburg",
                "status": "In Transit",
            },
        )
        assert response.status_code == 400
        assert (
            "Cargo ID 999 does not exist" in response.json()["detail"]
            or "Vessel ID 999 does not exist" in response.json()["detail"]
        )

    def test_create_tracking_with_valid_cargo_and_vessel(
        self, client: TestClient
    ) -> None:
        """A tracking entry should be created only if both cargo_id and vessel_id exist."""
        # First, create a contract and cargo
        contract_response = client.post(
            "/contracts/",
            json={
                "client_id": 1,
                "destination": "New York",
                "price": 1000.0,
                "status": "active",
            },
        )
        assert contract_response.status_code == 200
        contract_id: int = contract_response.json()["contract_id"]

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
        cargo_id: int = cargo_response.json()["cargo_id"]

        # Create a vessel
        vessel_response = client.post(
            "/vessels/",
            json={
                "name": "Ocean Explorer",
                "capacity": 10000.0,
                "current_location": "Port of Rotterdam",
            },
        )
        assert vessel_response.status_code == 200
        vessel_id: int = vessel_response.json()["vessel_id"]

        # Now create tracking with valid cargo and vessel
        tracking_response = client.post(
            "/tracking/",
            json={
                "cargo_id": cargo_id,
                "vessel_id": vessel_id,
                "location": "Port of Hamburg",
                "status": "In Transit",
            },
        )
        assert tracking_response.status_code == 200
        assert "tracking_id" in tracking_response.json()

    def test_get_tracking(self, client: TestClient) -> None:
        """Retrieve a tracking entry by ID."""
        response = client.get("/tracking/1")
        assert response.status_code == 200

    def test_list_tracking(self, client: TestClient) -> None:
        """List all tracking entries."""
        response = client.get("/tracking/")
        assert response.status_code == 200

    def test_update_tracking(self, client: TestClient) -> None:
        """Update a tracking entry's status."""
        response = client.put("/tracking/1", json={"status": "Delivered"})
        assert "Delivered" in response.text
        assert response.status_code == 200

    def test_delete_tracking(self, client: TestClient) -> None:
        """Delete a tracking entry by ID."""
        response = client.delete("/tracking/1")
        assert response.status_code == 200
