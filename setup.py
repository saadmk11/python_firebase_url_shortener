import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="python_firebase_url_shortener",
    version="1.0.0",
    author="saadmk11",
    author_email="saad.mk112@gmail.com",
    description="A Python Client for Firebase Dynamic Links to Shorten URLs.",
    long_description=long_description,
    include_package_data=True,
    license='GNU Public License',
    long_description_content_type="text/markdown",
    url="https://github.com/saadmk11/firebase_url_shortener",
    packages=['python_firebase_url_shortener'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests==2.21.0"
    ]
)
