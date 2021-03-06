from hestia.service_interface import Service

from query.exceptions import QueryError
from query.managers.build import BuildQueryManager
from query.managers.experiment import ExperimentQueryManager
from query.managers.experiment_group import ExperimentGroupQueryManager
from query.managers.job import JobQueryManager
from query.managers.tensorboad import TensorboardQueryManager
from query.parser import parse_field


class QueryService(Service):
    __all__ = ('setup', 'filter_queryset', 'parse_field')

    MANAGER_MAPPING = {
        ExperimentQueryManager.NAME: ExperimentQueryManager,
        ExperimentGroupQueryManager.NAME: ExperimentGroupQueryManager,
        BuildQueryManager.NAME: BuildQueryManager,
        JobQueryManager.NAME: JobQueryManager,
        TensorboardQueryManager.NAME: TensorboardQueryManager,
    }

    @classmethod
    def filter_queryset(cls, manager, query_spec, queryset):
        if manager not in cls.MANAGER_MAPPING:
            raise QueryError('Manager `{}` was not configured'.format(manager))
        return cls.MANAGER_MAPPING[manager].apply(query_spec=query_spec, queryset=queryset)

    @classmethod
    def parse_field(cls, field):
        return parse_field(field=field)
