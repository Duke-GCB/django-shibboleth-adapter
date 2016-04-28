from setuptools import setup

setup(name='django-shibboleth-adapter',
        version='1.0.0',
        description='Adapter for integrating Shibboleth with the Django authentication system.',
        url='https://github.com/KonstantinSchubert/django-shibboleth-adapter',
        keywords='django shibboleth remoteuser',
        author='Konstantin Schubert',
        license='MIT',
        packages=['shibboleth', 'shibboleth.templates.shibboleth'],
    )
