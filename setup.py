import setuptools
import io
import os


package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, 'README.rst')
with io.open(readme_filename, encoding='utf-8') as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name="django-trace-id-middleware",
    version="0.1",
    author="Christie Grinham",
    author_email="christiegrinham@gmail.com",
    description="Middleware for attaching and logging trace id to requests",
    long_description=readme,
    url="https://github.com/cgrinham/django-request-trace-id-middleware",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
    ],
)
