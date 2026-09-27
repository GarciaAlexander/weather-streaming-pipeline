BOOTSTRAP_SERVERS = "localhost:29092"
TOPIC_NAME = "weather-events"
AWS_BUCKET_NAME = "kafka-stream-events"

API_KEY = "ADD YOUR OWN"  # later: move to environment variable
CITY = "Orlando"
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=imperial"

SCHEMA_REGISTRY_URL = "http://localhost:8081"
