import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_model

class PredictPipeline:
    def __init__(self) -> None:
        pass
    def predict(self, features):
        try:
            model_path='artifacts/model.pkl'
            preprocessor_path='artifacts/proprocessor.pkl'
            preprocessor=load_model(file_path=preprocessor_path)
            model=load_model(file_path=model_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)
        

# This class is responsible for mapping all the inputes got from UI to the backend with perticular values
class CustomData:
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    # This will return all my data in the form of a dataframe
    def get_data_as_data_frame(self):
        try:
            # Whatever inputs I am giving on my web application is getting mapped with these particular values and then creates a dataframe out of it
            custom_data_input_dict= {
                    "gender": [self.gender],
                    "race_ethnicity": [self.race_ethnicity],
                    "parental_level_of_education": [self.parental_level_of_education],
                    "lunch": [self.lunch],
                    "test_preparation_course": [self.test_preparation_course],
                    "reading_score": [self.reading_score],
                    "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)

