from aws_cdk import (
    core,
    aws_backup as backup,
    aws_kms as kms)
from aws_cdk.aws_events import Schedule
from aws_cdk.core import RemovalPolicy


class BackupStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # AWS backup
        # create a BackupVault
        key = kms.Key(self, 'COOL-BACKUP-KEY', removal_policy=RemovalPolicy.DESTROY)
        vault = backup.BackupVault(self, "BackupVault", backup_vault_name="COOL-VAULT", encryption_key=key)

        # create a BackupPlan
        plan = backup.BackupPlan(self, "COOL-BACKUP-PLAN", backup_plan_name="COOL-BACKUP-PLAN")

        # add backup resources with two way for two resources
        plan.add_selection("Selection", resources=[
            backup.BackupResource.from_tag("createdWith", "CDK")])

        # details with backup rules
        plan.add_rule(backup.BackupPlanRule(backup_vault=vault,
                                            rule_name="CDK_Backup_Rule",
                                            schedule_expression=Schedule.cron(minute="0", hour="16", day="1",
                                                                              month="1-12"),
                                            delete_after=core.Duration.days(130),
                                            move_to_cold_storage_after=core.Duration.days(10)))
