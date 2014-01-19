from sklearn import ensemble
import classes
from models.Base import BaseModel


class GridSample75Mixin(object):
    @staticmethod
    def process_image(img):
        return img.grid_sample(20, 2).flatten().astype('float64') / 255


class RandomForestModel(BaseModel, GridSample75Mixin):
    train_predictors_file = 'data/data_random_forest_train_001.npy'
    test_predictors_file = 'data/data_random_forest_test_001.npy'
    n_features = 75
    estimator_defaults = {
        'n_estimators': 250,
        'random_state': 0,
        'verbose': 3,
        'oob_score': True,
    }
    estimator_class = ensemble.RandomForestRegressor


class ExtraTreesModel(BaseModel, GridSample75Mixin):
    train_predictors_file = 'data/data_random_forest_train_001.npy'
    test_predictors_file = 'data/data_random_forest_test_001.npy'
    n_features = 75
    estimator_defaults = {
        'n_estimators': 15,
        'random_state': 0,
        'verbose': 3,
        }
    estimator_class = ensemble.ExtraTreesRegressor