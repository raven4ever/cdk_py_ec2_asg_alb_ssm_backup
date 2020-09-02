# SSM managed EC2 AutoScaling Group

## Scope

The scope of the project is to create an EC2 auto-scaling group managed using SSM with AWS Backup enabled.

## Stacks

There are 2 stacks available:

- [Backup Stack](stacks/backup_stack.py)
- [EC2 Creation Stack](stacks/ec2_asg_alb_stack.py)

## Execution

To deploy the stacks you can use one of the following commands:
- `cdk deploy cdk-backup-stack`: deploys only the backup stack
- `cdk deploy cdk-ec2-asg-alb-stack`: deploys only the auto-scaling group stack
- `cdk deploy cdk-ec2-asg-alb-stack cdk-backup-stack`: deploys both stacks

To destroy the resources created by the stacks use on the following commands:
- `cdk destroy cdk-backup-stack`: destroys only the backup stack
- `cdk destroy cdk-ec2-asg-alb-stack`: destroys only the auto-scaling group stack
- `cdk destroy cdk-ec2-asg-alb-stack cdk-backup-stack`: destroys both stacks

To skip the deploy/destroy confirmation add the following to the commands: `--require-approval=never`.

Enjoy!
