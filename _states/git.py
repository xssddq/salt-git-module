'''
Git Management
================

Manage git repositories:

.. code-block:: yaml

    /path/to/dest/:
      git:
        - exists
        - repo: git://github.com/user/repo.git
'''


def exists(name, repo):
    """
    Clone a git repository

    name
        The destination on the minion filesystem to clone to

    repo
        The URL of the repository to clone
    """

    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}

    # Make sure that opts is correct, it can be a list or a comma delimited
    # string
    if isinstance(opts, basestring):
        opts = opts.split(',')

    try:
        ret['changes'] = __salt__['git.clone'](repo=repo, dest=name)
    except:
        ret['result'] = False
        ret['comment'] = 'Failed to clone repository.'

    return ret
