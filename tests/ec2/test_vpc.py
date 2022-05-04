from unittest import TestCase

import aws_cdk as cdk
from aws_cdk import assertions
from aws_cdk import aws_ec2 as ec2

from blueprint.ec2 import Vpc


class VpcTestCase(TestCase):

    def setUp(self):
        self.app = cdk.App()
        self.stack = cdk.Stack(self.app, 'stack')

    def test_blueprint(self):
        # When
        blueprint = Vpc(self.stack, 'vpc')

        # Then
        self.assertEqual(blueprint.scope, self.stack)
        self.assertEqual(blueprint.id, 'vpc')
        self.assertEqual(blueprint.cidr, '10.0.0.0/16')

    def test_construct(self):
        # When
        blueprint = Vpc(self.stack, 'vpc')
        vpc = blueprint.build()

        # Then
        self.assertIsInstance(vpc, ec2.Vpc)

        template = assertions.Template.from_stack(self.stack)
        template.has_resource("AWS::EC2::VPC", {})
        template.resource_count_is("AWS::EC2::VPC", 1)

    def test_build_vpc_with_cidr(self):
        # Given
        cidr = '10.0.1.0/24'

        # When
        blueprint = Vpc(self.stack, 'vpc')
        blueprint.build(cidr=cidr)

        # Then
        self.assertEqual(blueprint.cidr, cidr)

        template = assertions.Template.from_stack(self.stack)
        template.has_resource_properties("AWS::EC2::VPC", {
            "CidrBlock": cidr
        })

    def test_build_vpc_from_lookup(self):
        # Tests no specifying the env property at all.

        # You can't write code like `if (stack.region == 'us-east-1')`
        # of use framework facilities like `Vpc.from_lookup`,
        # which need to query you AWS account

        self.assertTrue(hasattr(Vpc, 'from_lookup'))
        self.assertTrue(callable(getattr(Vpc, 'from_lookup')))
