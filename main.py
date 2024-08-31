import modelbit as mb
import random

def predict_weather(days_from_now: int):
  prediction = random.choice(["sunny", "cloudy", "just right"])
  return {
    "weather": prediction,
    "message": f"In {days_from_now} days it will be {prediction}!"
  }

mb.deploy(predict_weather)