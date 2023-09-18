import setuptools

from _version import __version__


with open("README.md", encoding="utf8") as f:
    README = f.read()


requirements = []
with open("requirements.txt") as f:
    for line in f.read().splitlines():
        requirements.append(line)


setuptools.setup(
    name="movie-service",
    version=__version__,
    author="Petar Peychev",
    author_email="petarpeychev98@gmail.com",
    description="Example REST API built using Python, FastAPI and PostgreSQL.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PetarPeychev/fastapi-movies",
    packages=["movie_service"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: The Unlicense",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires="~=3.10",
)
