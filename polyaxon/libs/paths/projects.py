import os

from django.conf import settings

import stores

from libs.paths.utils import delete_path


def get_project_outputs_path(persistence_outputs, project_name):
    persistence_outputs = stores.get_outputs_paths(persistence_outputs)
    return os.path.join(persistence_outputs, project_name.replace('.', '/'))


def get_project_logs_path(project_name):
    persistence_logs = stores.get_logs_paths()
    return os.path.join(persistence_logs, project_name.replace('.', '/'))


def get_project_repos_path(project_name):
    return os.path.join(settings.REPOS_MOUNT_PATH, project_name.replace('.', '/'))


def delete_project_outputs(persistence_outputs, project_name):
    path = get_project_outputs_path(persistence_outputs, project_name)
    delete_path(path)


def delete_project_logs(project_name):
    path = get_project_logs_path(project_name)
    delete_path(path)


def delete_project_repos(project_name):
    path = get_project_repos_path(project_name)
    delete_path(path)
