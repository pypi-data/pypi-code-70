# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['authl', 'authl.handlers']

package_data = \
{'': ['*'], 'authl': ['flask_templates/*', 'icons/*']}

install_requires = \
['beautifulsoup4>=4.9.1,<5.0.0',
 'expiringdict>=1.2.1,<2.0.0',
 'itsdangerous>=1.1.0,<2.0.0',
 'mastodon.py>=1.5.1,<2.0.0',
 'mf2py>=1.1.2,<2.0.0',
 'requests>=2.24.0,<3.0.0',
 'requests_oauthlib>=1.3.0,<2.0.0',
 'validate_email>=1.3,<2.0']

setup_kwargs = {
    'name': 'authl',
    'version': '0.4.6',
    'description': 'Framework-agnostic authentication wrapper',
    'long_description': '# Authl\nA Python library for managing federated identity\n\n[![Documentation Status](https://readthedocs.org/projects/authl/badge/?version=latest)](https://authl.readthedocs.io/en/latest/?badge=latest)\n\n## About\n\nAuthl is intended to make it easy to add federated identity to Python-based web\napps without requiring the creation of site-specific user accounts, but also\nwithout requiring the user to choose from a myriad of buttons or links to select\nany specific login provider.\n\nAll it should take is a single login form that asks for how the user wants to be\nidentified.\n\n## Current state\n\nThe basic API works, and provides an easy drop-in set of endpoints for\n[Flask](http://flask.pocoo.org).\n\nCurrently supported authentication mechanisms:\n\n* Directly authenticating against email using a magic link\n* Federated authentication against Fediverse providers\n    ([Mastodon](https://joinmastodon.org/), [Pleroma](https://pleroma.social))\n* Federated authentication against [IndieAuth](https://indieauth.net/)\n* Silo authentication against [Twitter](https://twitter.com/)\n* Test/loopback authentication for development purposes\n\nPlanned functionality:\n\n* Pluggable OAuth mechanism to easily support additional identity providers such as:\n    * OpenID Connect (Google et al)\n    * Facebook\n    * GitHub\n* OpenID 1.x (Wordpress, LiveJournal, Dreamwidth, etc.)\n* A more flexible configuration system\n\n## Rationale\n\nIdentity is hard, and there are so many competing standards which try to be the\nbe-all end-all Single Solution. OAuth and OpenID Connect want lock-in to silos,\nIndieAuth wants every user to self-host their own identity site, and OpenID 1.x\nhas fallen by the wayside. Meanwhile, users just want to be able to log in with\nthe social media they\'re already using (siloed or not).\n\nAny solution which requires all users to have a certain minimum level of\ntechnical ability is not a workable solution.\n\nAll of these solutions are prone to the so-called "[NASCAR\nproblem](https://indieweb.org/NASCAR_problem)" where every supported login\nprovider needs its own UI. But being able to experiment with a more unified UX\nmight help to fix some of that.\n\n## Documentation\n\nFull API documentation is hosted on [readthedocs](https://authl.readthedocs.io).\n\n## Usage\n\nBasic usage is as follows:\n\n1. Create an Authl object with your configured handlers\n\n    This can be done by instancing individual handlers yourself, or you can use\n    `authl.from_config`\n\n2. Make endpoints for initiation and progress callbacks\n\n    The initiation callback receives an identity string (email address/URL/etc.)\n    from the user, queries Authl for the handler and its ID, and builds a\n    callback URL for that handler to use. Typically you\'ll have a single\n    callback endpoint that includes the handler\'s ID as part of the URL scheme.\n\n    The callback endpoint needs to be able to receive a `GET` or `POST` request\n    and use that to validate the returned data from the authorization handler.\n\n    Your callback endpoint (and generated URL thereof) should also include\n    whatever intended forwarding destination.\n\n3. Handle the `authl.disposition` object types accordingly\n\n    A `disposition` is what should be done with the agent that initiated the\n    endpoint call. Currently there are the following:\n\n    * `Redirect`: return an HTTP redirection to forward it along to another URL\n    * `Notify`: return a notification to the user that they must take another\n      action (e.g. check their email)\n    * `Verified`: indicates that the user has been verified; set a session\n      cookie (or whatever) and forward them along to their intended destination\n    * `Error`: An error occurred; return it to the user as appropriate\n\n## Flask usage\n\nTo make life easier with Flask, Authl provides an `authl.flask.AuthlFlask`\nwrapper. You can use it from a Flask app with something like the below:\n\n```python\nimport uuid\nimport logging\n\nimport flask\nimport authl.flask\n\nlogging.basicConfig(level=logging.INFO)\nLOGGER = logging.getLogger(__name__)\n\napp = flask.Flask(\'authl-test\')\n\napp.secret_key = str(uuid.uuid4())\nauthl = authl.flask.AuthlFlask(\n    app,\n    {\n        \'SMTP_HOST\': \'localhost\',\n        \'SMTP_PORT\': 25,\n        \'EMAIL_FROM\': \'authl@example.com\',\n        \'EMAIL_SUBJECT\': \'Login attempt for Authl test\',\n        \'INDIELOGIN_CLIENT_ID\': \'http://localhost\',\n        \'TEST_ENABLED\': True,\n        \'MASTODON_NAME\': \'authl testing\',\n        \'MASTODON_HOMEPAGE\': \'https://github.com/PlaidWeb/Authl\'\n    },\n    tester_path=\'/check_url\'\n)\n\n\n@app.route(\'/\')\n@app.route(\'/some-page\')\ndef index():\n    """ Just displays a very basic login form """\n    LOGGER.info("Session: %s", flask.session)\n    LOGGER.info("Request path: %s", flask.request.path)\n\n    if \'me\' in flask.session:\n        return \'Hello {me}. Want to <a href="{logout}">log out</a>?\'.format(\n            me=flask.session[\'me\'], logout=flask.url_for(\n                \'logout\', redir=flask.request.path[1:])\n        )\n\n    return \'You are not logged in. Want to <a href="{login}">log in</a>?\'.format(\n        login=flask.url_for(\'authl.login\', redir=flask.request.path[1:]))\n\n\n@app.route(\'/logout/\')\n@app.route(\'/logout/<path:redir>\')\ndef logout(redir=\'\'):\n    """ Log out from the thing """\n    LOGGER.info("Logging out")\n    LOGGER.info("Redir: %s", redir)\n    LOGGER.info("Request path: %s", flask.request.path)\n\n    flask.session.clear()\n    return flask.redirect(\'/\' + redir)\n```\n\nThis will configure the Flask app to allow IndieLogin, Mastodon, and email-based\nauthentication (using the server\'s local sendmail), and use the default login\nendpoint of `/login/`. The `index()` endpoint handler always redirects logins\nand logouts back to the same page when you log in or log out (the `[1:]` is to\ntrim off the initial `/` from the path). The logout handler simply clears the\nsession and redirects back to the redirection path.\n\nThe above configuration uses Flask\'s default session lifetime of one month (this\ncan be configured by setting `app.permanent_session_lifetime` to a `timedelta`\nobject, e.g. `app.permanent_session_lifetime = datetime.timedelta(hours=20)`).\nSessions will also implicitly expire whenever the application server is\nrestarted, as `app.secret_key` is generated randomly at every startup.\n\n### Accessing the default stylesheet\n\nIf you would like to access `authl.flask`\'s default stylesheet, you can do it by\npassing the argument `asset=\'css\'` to the login endpoint. For example, if you\nare using the default endpoint name of `authl.login`, you can use:\n\n```python\nflask.url_for(\'authl.login\', asset=\'css\')\n```\n\nfrom Python, or e.g.\n\n```html\n<link rel="stylesheet" href="{{url_for(\'authl.login\', asset=\'css\')}}">\n```\n\nfrom a Jinja template.\n\n## Notes\n\nAt present, the Twitter handler doesn\'t perform well on load-balanced setups\nor on certain cloud-based app providers.\n',
    'author': 'fluffy',
    'author_email': 'fluffy@beesbuzz.biz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://plaidweb.site/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
