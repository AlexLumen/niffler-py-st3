import json
import pytest
from allure import step, epic, suite, title, id, tag

from models.user import UserName

pytestmark = [pytest.mark.allure_label("Kafka", label_type="epic")]

KAFKA_TOPIC = "users"



@id("600001")
@title("KAFKA: Сообщение с пользователем публикуется в Kafka после успешной регистрации")
@tag("KAFKA")
def test_message_should_be_produced_to_kafka_after_successful_registration(user_data, auth_client, kafka):
    username = user_data.username
    password = user_data.password
    topic_partitions = kafka.subscribe_listen_new_offsets(KAFKA_TOPIC)
    result = auth_client.register(username, password)
    assert result.status_code == 201
    event = kafka.log_msg_and_json(topic_partitions)
    with step("Проверить, что сообщение из кафки присутствует"):
        assert event != '' and event != b''
    with step("Проверить содержание сообщения"):
        UserName.model_validate(json.loads(event.decode('utf8')))
        assert json.loads(event.decode('utf8'))['username'] == username


@id("600002")
@title("KAFKA: Заполнение userdata исключая auth")
@tag("KAFKA")
def test_message_should_be_produced_to_userdata_after_kafka_event(user_data, kafka, authority_db, user_db):
    username = user_data.username
    print("username", username)
    kafka.sent_event(KAFKA_TOPIC, username)

    with step("Check new record in auth db"):
        assert authority_db.get_user_by_user_name(username) is None

    with step("Check new record in userdata db"):
        assert user_db.get_user_by_username(username).username == username
