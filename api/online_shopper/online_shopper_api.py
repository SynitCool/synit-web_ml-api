import numpy as np

from flask import Blueprint
from flask import jsonify
from flask import request

from .preprocessing import load_object

from .config import X_OBJECT_COLUMNS
from .config import X_OBJECT_INDEX

import warnings

online_shopper_api = Blueprint("online_shopper_api", __name__)


@online_shopper_api.route("/api/online_shopper/online_shopper_api", methods=["POST"])
def online_shopper_model():
    # Handle warnings
    warnings.filterwarnings("ignore", category=UserWarning)

    # loading json
    data = request.get_json(force=True)

    X_data = data["input"]

    # declare model
    model_path = "api/online_shopper/object_save/model_object_rfc"
    model = load_object(model_path)

    # cleaning data
    for index, column in zip(X_OBJECT_INDEX, X_OBJECT_COLUMNS):
        file_path = f"api/online_shopper/object_save/encoder_columns_{column}"
        le = load_object(file_path)

        X_data[index] = le.transform([X_data[index]])

    X_data = np.reshape(X_data, (1, -1))

    # modelling
    y_pred = model.predict(X_data)

    # encode label
    file_path = "api/online_shopper/object_save/encoder_columns_label"
    le = load_object(file_path)
    y_pred = le.transform([y_pred[0]])

    return jsonify(results=str(y_pred[0]))
