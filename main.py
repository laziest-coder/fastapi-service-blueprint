from fastapi import FastAPI
import uvicorn
from app.v1.example_controller import get_example_order_id
import settings

app = FastAPI()

@app.get("/v1/example-route")
def predict_cooking_time(order_id: int):
    return get_example_order_id(order_id)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)
