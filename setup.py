from setuptools import setup, find_packages

setup(name="census-income",
            version = "0.0.1",
            author ="vishal",
            author_email="vish@gmail.com",
            packages=find_packages(),
            install_requirments=["pandas","numpy","flask"]
    )