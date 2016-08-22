# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

from coriolis import constants
from coriolis import exception
from coriolis.tasks import migration_tasks
from coriolis.tasks import replica_tasks

_TASKS_MAP = {
    constants.TASK_TYPE_EXPORT_INSTANCE:
        migration_tasks.ExportInstanceTask,
    constants.TASK_TYPE_IMPORT_INSTANCE:
        migration_tasks.ImportInstanceTask,
    constants.TASK_TYPE_GET_INSTANCE_INFO:
        replica_tasks.GetInstanceInfoTask,
    constants.TASK_TYPE_REPLICATE_DISKS:
        replica_tasks.ReplicateDisksTask,
    constants.TASK_TYPE_SHUTDOWN_INSTANCE:
        replica_tasks.ShutdownInstanceTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_DISKS:
        replica_tasks.DeployReplicaDisksTask,
    constants.TASK_TYPE_DELETE_REPLICA_DISKS:
        replica_tasks.DeleteReplicaDisksTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_TARGET_RESOURCES:
        replica_tasks.DeployReplicaTargetResourcesTask,
    constants.TASK_TYPE_DELETE_REPLICA_TARGET_RESOURCES:
        replica_tasks.DeleteReplicaTargetResourcesTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_SOURCE_RESOURCES:
        replica_tasks.DeployReplicaSourceResourcesTask,
    constants.TASK_TYPE_DELETE_REPLICA_SOURCE_RESOURCES:
        replica_tasks.DeleteReplicaSourceResourcesTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_INSTANCE:
        replica_tasks.DeployReplicaInstanceTask,
    constants.TASK_TYPE_CREATE_REPLICA_DISK_SNAPSHOTS:
        replica_tasks.CreateReplicaDiskSnapshotsTask,
    constants.TASK_TYPE_DELETE_REPLICA_DISK_SNAPSHOTS:
        replica_tasks.DeleteReplicaDiskSnapshotsTask,
}


def get_task_runner(task_type):
    cls = _TASKS_MAP.get(task_type)
    if not cls:
        raise exception.NotFound(
            "TaskRunner not found for task type: %s" % task_type)
    return cls()
