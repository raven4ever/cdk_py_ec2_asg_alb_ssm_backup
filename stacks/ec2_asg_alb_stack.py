import os
from pathlib import Path

from aws_cdk import (
    core,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elb,
    aws_autoscaling as asg)


class CdkEc2AsgAlbStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, 'COOL-VPC')

        # IAM
        instance_role = iam.Role(self, 'instance_role', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))
        instance_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AmazonEC2RoleforSSM'))

        # Security Group
        lb_sg = ec2.SecurityGroup(self, 'lbSg', vpc=vpc, allow_all_outbound=True,
                                  description='Load Balancer Security Group')
        lb_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80))

        instance_sg = ec2.SecurityGroup(self, 'instanceSg', vpc=vpc, allow_all_outbound=True,
                                        description='Instance Security Group')
        instance_sg.add_ingress_rule(lb_sg, ec2.Port.tcp(80))

        # Auto Scaling Group
        ec2_scaling_group = asg.AutoScalingGroup(self, 'COOL-ASG', vpc=vpc, role=instance_role,
                                                 max_capacity=10, min_capacity=1, desired_capacity=1,
                                                 instance_type=ec2.InstanceType('t2.micro'),
                                                 machine_image=ec2.AmazonLinuxImage(
                                                     generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2))
        ec2_scaling_group.add_security_group(instance_sg)

        # User data
        dirname = os.path.dirname(__file__)
        user_data = Path(os.path.join(dirname, "assets/user_data.sh")).read_text()
        ec2_scaling_group.add_user_data(user_data)

        # Application Load Balancer
        app_lb = elb.ApplicationLoadBalancer(self, 'Cool LB', vpc=vpc, internet_facing=True, security_group=lb_sg)
        lb_listener = app_lb.add_listener('listener1', port=80, protocol=elb.ApplicationProtocol.HTTP, open=True)
        lb_listener.add_targets('webServers', port=80, protocol=elb.ApplicationProtocol.HTTP,
                                targets=[ec2_scaling_group])

        # Outputs
        core.CfnOutput(self, 'LB-DNS', value=app_lb.load_balancer_dns_name)
