from setuptools import setup

setup(
    name = "trlo",
    description = "A minimalist Trello API client.",
    version = "1.1",
    author = "Jacob Kaplan-Moss",
    author_email = "jacob@jacobian.org",
    url = "http://github.com/jacobian/trlo",
    py_modules = ['trlo'],
    install_requires = ['requests>=1.2', 'requests-oauthlib>=0.3.2'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
