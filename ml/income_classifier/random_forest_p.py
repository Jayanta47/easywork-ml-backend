
import joblib
import pandas as pd

class RandomForestClassifierPriority: 
    def __init__(self):
        path_to_artifacts = "./research/"
        self.model = joblib.load(path_to_artifacts + "priority_random_forest.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])
        # fill missing values
        # input_data.fillna(self.values_fill_missing)
        # convert categoricals
        # for column in [
        #     "workclass",
        #     "education",
        #     "marital-status",
        #     "occupation",
        #     "relationship",
        #     "race",
        #     "sex",
        #     "native-country",
        # ]:
        #     categorical_convert = self.encoders[column]
        #     input_data[column] = categorical_convert.transform(input_data[column])

        return input_data

    def predict(self, input_data):
        return self.model.predict(input_data)

    def postprocessing(self, input_data):
        if input_data[0] == 0:
            label = "Low"
        elif input_data[0] == 1:
            label = "Medium"
        elif input_data[0] == 2:
            label = "High"
        else:
            label = "Very High"
        return {"label": label, "point": input_data[0], "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            print(str(e))
            return {"status": "Error", "message": str(e)}

        return prediction