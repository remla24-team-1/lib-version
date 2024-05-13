from setuptools import setup, find_packages

setup(
    name='remlaversionutilpy',
    use_scm_version={
        'version_scheme': 'guess-next-dev',
        'local_scheme': lambda version: '',
    },
    setup_requires=['setuptools_scm'],

    packages=find_packages(),
)
