import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="ec2_asg_alb_backup",
    version="0.0.1",

    description="Deploy EC2 AutoScaling Group managed by SSM with Backup enabled",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="raven4ever",

    package_dir={"": "stacks"},
    packages=setuptools.find_packages(where="stacks"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-iam",
        "aws-cdk.aws-ec2",
        "aws-cdk.aws-elasticloadbalancingv2",
        "aws-cdk.aws-autoscaling",
        "aws-cdk.aws-backup",
        "aws-cdk.aws-kms"
    ],

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: Finished",

        "Intended Audience :: Developers",

        "Programming Language :: Python :: 3.8"
    ],
)
