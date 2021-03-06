# Copyright 2018 ASI Data Science
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import find_packages, setup

setup(
    name="faculty-mill",
    description=(
        "Run and publish parameterised Jupyter notebooks "
        "using Faculty Platform."
    ),
    author="ASI Data Science",
    author_email="opensource@asidatascience.com",
    license="Apache Software License",
    packages=find_packages(),
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    install_requires=["click", "papermill", "faculty"],
    entry_points={"console_scripts": ["faculty-mill=faculty_mill.cli:cli"]},
)
