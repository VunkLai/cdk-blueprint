import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_construct_classes.cdk_construct_classes_stack import CdkConstructClassesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_construct_classes/cdk_construct_classes_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkConstructClassesStack(app, "cdk-construct-classes")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
