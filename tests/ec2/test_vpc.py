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

    def test_construct(self):
        # When
        blueprint = Vpc(self.stack, 'vpc')
        vpc = blueprint.build()

        # Then
        self.assertIsInstance(vpc, ec2.Vpc)

        template = assertions.Template.from_stack(self.stack)
        template.has_resource("AWS::EC2::VPC", {})
