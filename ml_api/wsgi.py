"""
WSGI config for ml_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ml_api.settings')

application = get_wsgi_application()

# The registry code is ready, we need to specify one place 
# in the server code which will add ML algorithms to the 
# registry when the server is starting.


# ML registry
import inspect
from ml.registry import MLRegistry
from ml.income_classifier.random_forest import RandomForestClassifier
from ml.income_classifier.random_forest_p import RandomForestClassifierPriority

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    rfp = RandomForestClassifierPriority()

    registry.add_algorithm(endpoint_name="priority_classifier",
                            algorithm_object=rfp,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Jayanta",
                            algorithm_description="Random Forest Classifier to detect task priority",
                            algorithm_code=inspect.getsource(RandomForestClassifierPriority))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
