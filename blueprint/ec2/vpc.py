from typing import Optional

from aws_cdk import aws_ec2 as ec2

import attrs

from blueprint import Infrastructure


@attrs.define
class Vpc(Infrastructure):
    """
    https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/Vpc.html#vpc
    """
    cidr: Optional[str] = attrs.field(default=ec2.Vpc.DEFAULT_CIDR_RANGE)
    # max_azs: Optional[int] = attrs.field(default=2, converter=int)

    def build(self, **kwargs) -> ec2.Vpc:
        for key, val in kwargs.items():
            setattr(self, key, val)
        return ec2.Vpc(**self.kwargs)

    def from_lookup(self, vpc_id: str) -> ec2.Vpc:
        return ec2.Vpc.from_lookup(self.scope, self.id, vpc_id=vpc_id)
