import json
import pytest
import allure

from models.user import UserName

pytestmark = [pytest.mark.allure_label("Kafka", label_type="epic")]

KAFKA_TOPIC = "users"


@allure.epic("Kafka")
@allure.title("KAFKA: Сообщение с пользователем публикуется в Kafka после успешной регистрации")
def test_message_should_be_produced_to_kafka_after_successful_registration(user_data, auth_client, kafka):
    username = user_data.username
    password = user_data.password
    topic_partitions = kafka.subscribe_listen_new_offsets(KAFKA_TOPIC)
    result = auth_client.register(username, password)
    assert result.status_code == 201
    event = kafka.log_msg_and_json(topic_partitions)
    assert event != '' and event != b''
    UserName.model_validate(json.loads(event.decode('utf8')))
    assert json.loads(event.decode('utf8'))['username'] == username


@allure.epic("Kafka")
@allure.title("KAFKA: Заполнение userdata исключая auth")
def test_message_should_be_produced_to_userdata_after_kafka_event(user_data, kafka, authority_db, user_db):
    username = user_data.username
    kafka.sent_event(KAFKA_TOPIC, username)
    assert authority_db.get_user_by_user_name(username) is None
    assert user_db.get_user_by_username(username).username == username
