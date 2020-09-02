#!/usr/bin/env python3

from aws_cdk import core

from cdk_py_as_alb_ssm.cdk_py_as_alb_ssm_stack import CdkPyAsAlbSsmStack


app = core.App()
CdkPyAsAlbSsmStack(app, "cdk-py-as-alb-ssm")

app.synth()
