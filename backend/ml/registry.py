from endpoints.models import *

class MLRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algorithm(self, endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, owner,
                    algorithm_description, algorithm_code):
        # get endpoint
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)

        # get algorithm
        database_object, algorithm_created = MlAlgorithim.objects.get_or_create(
                name=algorithm_name,
                description=algorithm_description,
                code=algorithm_code,
                versions=algorithm_version,
                owner=owner,
                parentEndpoint=endpoint)
        if algorithm_created:
            status = MlAlgorithimStatus(status = algorithm_status,
                                        createdBy = owner,
                                        parentAlgo = database_object,
                                        active = True)
            status.save()

        self.endpoints[database_object.id] = algorithm_object