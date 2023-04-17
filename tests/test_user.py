from scootbot3.util.user import user_data_from_id


def test_user_data_from_id(client):
    user_data = user_data_from_id(client, "U1V06TSHF")
    assert user_data["name"] == "gilgi"
