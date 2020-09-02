#!/usr/bin/env python3

from datetime import datetime

from aws_cdk import core
from aws_cdk.core import Tag

from stacks.backup_stack import BackupStack
from stacks.ec2_asg_alb_stack import CdkEc2AsgAlbStack

app = core.App()

Tag.add(app, "createdBy", "raven4ever")
Tag.add(app, "createdWith", "CDK")
Tag.add(app, "createdAt", datetime.now().strftime("%d/%m/%Y-%H:%M:%S"))

ec2_stack = CdkEc2AsgAlbStack(app, "cdk-ec2-asg-alb-stack")
BackupStack(app, "cdk-backup-stack").add_dependency(ec2_stack)

app.synth()
