# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_sso_lib', 'aws_sso_lib.vendored_botocore']

package_data = \
{'': ['*']}

install_requires = \
['aws-error-utils>=1.0.4,<2.0.0', 'boto3>=1.16.13,<2.0.0']

setup_kwargs = {
    'name': 'aws-sso-lib',
    'version': '1.3.0',
    'description': 'Library to make AWS SSO easier',
    'long_description': '# `aws-sso-lib`\n\n`aws-sso-lib` allows you to programmatically interact with AWS SSO.\n\nThe primary functions that will be of interest are available at the package level:\n* `get_boto3_session`: Get a boto3 session for a specific account and role.\n* `login`: ensure the user is logged in to AWS SSO, with dispatch to the browser.\n* `list_available_accounts` and `list_available_roles`: discover the access the user has.\n* `list_assignments`: for admin purposes, iterate over all assignments in AWS SSO, which is currently hard to do through the API.\n\n`aws-sso-util` is a command-line utility built on `aws-sso-lib` for interacting with AWS SSO; see the details of that project [here](https://github.com/benkehoe/aws-sso-util).\n\n## Install\n\n```\npip install --user aws-sso-lib\npython -c "import aws_sso_lib; aws_sso_lib.login(\'https://my-start-url.awsapps.com/start\', \'us-east-2\')"\n```\n\n## `get_boto3_session`\n\nOften when writing a script, you know the exact account and role you want the script to use.\nYou could configure a profile in your `~/.aws/config` for this (perhaps using `aws-sso-util configure profile`), but especially if multiple people may be using the script, it\'s more convenient to have the configuration baked into the script itself.\n`get_boto3_session()` is the function to do that with.\n\n```python\nget_boto3_session(start_url, sso_region, account_id, role_name, region, login=False)\n```\n\n* `start_url`: [REQUIRED] The start URL for the AWS SSO instance.\n* `sso_region`: [REQUIRED] The AWS region for the AWS SSO instance.\n* `account_id`: [REQUIRED] The AWS account ID to use.\n* `role_name`: [REQUIRED] The AWS SSO role (aka PermissionSet) name to use.\n* `region`: [REQUIRED] The AWS region for the boto3 session.\n* `login`: Set to `True` to interactively log in the user if their AWS SSO credentials have expired.\n* Returns a [boto3 Session object](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html) configured for the account and role.\n\nFor more control over the login process, use the `login` function separately.\n\n## `login`\n\nWhile the functions that require the user to be logged in let you specify `login=True` to interactively log in the user if they are not already logged in, you can have more control over the process, or retrieve the access token, using `login()`.\n\nIf the user is not logged in or `force_refresh` is `True`, it will attempt to log in.\nIf the user is logged in and `force_refresh` is `False`, no action is taken.\n\nNormally, it will attempt to automatically open the user\'s browser to log in, as well as printing the URL and code to stderr as a fallback. However, if `disable_browser` is `True`, or if `disable_browser` is `None` (the default) and the environment variable `AWS_SSO_DISABLE_BROWSER` is set to `1` or `true`, only the message with the URL and code will be printed.\n\nA custom message can be printed by setting `message` to a template string using `{url}` and `{code}` as placeholders.\nThe message can be suppressed by setting `message` to `False`.\n\n```python\nlogin(start_url, sso_region, force_refresh=False, disable_browser=None, message=None, outfile=None)\n```\n\n* `start_url`: [REQUIRED] The start URL for the AWS SSO instance.\n* `sso_region`: [REQUIRED] The AWS region for the AWS SSO instance.\n* `force_refresh`: Set to `True` to always go through the authentication process.\n* `disable_browser`: Set to `True` to skip the browser popup and only print a message with the URL and code.\n* `message`: A message template to print with the fallback URL and code, or `False` to suppress the message.\n* `outfile`: The file-like object to print the message to (stderr by default)\n* Returns the token dict as returned by [sso-oidc:CreateToken](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html), which contains the actual authorization token, as well as the expiration.\n\n## `list_available_accounts` and `list_available_roles`\n\nAWS SSO provides programmatic access to the permissions that a user has.\nYou can access this through `list_available_accounts()` and `list_available_roles()`.\n\nWith both, you can set `login=True` to interactively log in the user if they are not already logged in.\n\nNote that these functions return iterators; they don\'t return a list, because the number of roles may be very large and you shouldn\'t have to wait for the entire list to be created to start processing.\nYou can always get a list by, for example, `list(list_available_roles(...))`.\n\n```python\nlist_available_accounts(start_url, sso_region, login=False)\n```\n\n* `start_url`: The start URL for the AWS SSO instance.\n* `sso_region`: The AWS region for the AWS SSO instance.\n* `login`: Set to `True` to interactively log in the user if their AWS SSO credentials have expired.\n* Returns an iterator that yields account id and account name.\n\n```\nlist_available_roles(start_url, sso_region, account_id=None, login=False)\n```\n\n* `start_url`: [REQUIRED] The start URL for the AWS SSO instance.\n* `sso_region`: [REQUIRED] The AWS region for the AWS SSO instance.\n* `account_id`: Optional account id or list of account ids to check.\n  * If not set, all accounts available to the user are used.\n* `login`: Set to `True` to interactively log in the user if their AWS SSO credentials have expired.\n* Returns an iterator that yields account id, account name, and role name.\n\n## `list_assignments`\n\nThe AWS SSO API only allows you to [list assignments for a specific account _and_ permission set](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignments.html).\nTo find all your assignments, you need to iterate over all accounts, and then interate over all permission sets.\n`list_assignments()` does this work for you.\n\nUnlike the other functions list above, this uses admin APIs, which require AWS credentials, rather than taking as input a start URL and region.\n\n`list_assignments` returns an iterator over `Assignment` named tuples, which have the following fields:\n\n* `instance_arn`\n* `principal_type`\n* `principal_id`\n* `principal_name`\n* `permission_set_arn`\n* `permission_set_name`\n* `target_type`\n* `target_id`\n* `target_name`\n\nThe name fields may be `None`, if the names are not known or looked up.\nBy default, principal and permission set names are not retrieved, nor are account names for accounts that have been provided as explicit targets.\n\nIf you don\'t specify `instance_arn` and/or `identity_store_id`, these will be looked up using the [ListInstances API](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html), which today returns at most one instance (with associated identity store).\n\nAn assignment is the combination of a principal (a user or a group), a permission set, and a target (an AWS account).\nFor each of these values, you can provide either an explicit specification, or a filter function.\n\nYou can provide an OU as a target, which will use all accounts in that OU, and optionally all accounts recursively in child OUs as well.\n\n```python\nlist_assignments(\n    session,\n    instance_arn=None,\n    identity_store_id=None,\n    principal=None,\n    principal_filter=None,\n    permission_set=None,\n    permission_set_filter=None,\n    target=None,\n    target_filter=None,\n    get_principal_names=False,\n    get_permission_set_names=False,\n    get_target_names=False,\n    ou_recursive=False)\n```\n\n* `session`: [REQUIRED] boto3 session to use\n* `instance_arn`: The SSO instance to use, or it will be looked up using ListInstances\n* `identity_store_id`: The identity store to use if principal names are being retrieved or it will be looked up using ListInstances\n* `principal`: A principal specification or list of principal specifications.\n  * A principal specification is a principal id or a 2-tuple of principal type and id.\n* `principal_filter`: A callable taking principal type, principal id, and principal name (which may be `None`), and returning `True` if the principal should be included.\n* `permission_set`: A permission set arn or id, or a list of the same.\n* `permission_set_filter`: A callable taking permission set arn and name (name may be `None`), returning True if the permission set should be included.\n* `target`: A target specification or list of target specifications.\n  * A target specification is an account or OU id, or a 2-tuple of target type, which is either AWS_ACCOUNT or AWS_OU, and target id.\n* `target_filter`: A callable taking target type, target id, and target name (which may be `None`), and returning `True` if the target should be included.\n* `get_principal_names`: Set to `True` to retrieve names for principals in assignments.\n* ` get_permission_set_names`: Set to `True` to retrieve names for permission sets in assignments.\n* `get_target_names`: Set to `True` to retrieve names for targets in assignments, when they are explicitly provided as targets. For OUs as targets or if no targets are specified, the account names will be retrieved automatically during the enumeration process.\n* `ou_recursive`: Set to `True` if an OU is provided as a target to get all accounts including those in child OUs.\n* Returns an iterator over `Assignment` tuples\n',
    'author': 'Ben Kehoe',
    'author_email': 'ben@kehoe.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/benkehoe/aws-sso-util',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
