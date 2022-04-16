#!/usr/bin/env python3

import aws_cdk as cdk

app = cdk.App()
env = cdk.Environment(account='123', region='foo')

stack = cdk.Stack(app, 'stack', env=env)

app.synth()
