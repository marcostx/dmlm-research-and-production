from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
import preprocessors as pp
import config


titanic_pipe = Pipeline(steps=
    [('categorical_imputer',
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),
         
    ('missing_column',
        pp.MissingIndicator(variables=config.NUMERICAL_VARS)),
    
    ('numerical_imputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS)),

    ('first_letter_extractor',
        pp.ExtractFirstLetter(variables=config.CABIN)),
    ('rare_label_encoder',
        pp.RareLabelCategoricalEncoder(
            tol=0.05,
            variables=config.CATEGORICAL_VARS)),
    ('categorical_encoder',
        pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
        
    ('scaler', StandardScaler()),
    ('linear_model', LogisticRegression(C=0.0005, random_state=0))
    ]
)