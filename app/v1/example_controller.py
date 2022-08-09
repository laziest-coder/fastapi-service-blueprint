from app.utils import logger

logger = logger.get_logger()


def get_example_order_id(order_id: int):
    # do some logic
    logger.info("Starting to execute the method")
    result = f"Order id is: {order_id}"
    return {"result": result}
