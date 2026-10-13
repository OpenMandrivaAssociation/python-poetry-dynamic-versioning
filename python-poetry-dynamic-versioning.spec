Name:		python-poetry-dynamic-versioning
Version:	1.10.0
Release:	2
Summary:	Plugin for Poetry to enable dynamic versioning based on VCS tags
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/poetry-dynamic-versioning/
Source0:	poetry_dynamic_versioning-1.10.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(dunamai)
BuildRequires:	python%{pyver}dist(tomlkit)
BuildRequires:	python%{pyver}dist(jinja2)
BuildArch:	noarch
%description
Plugin for Poetry to enable dynamic versioning based on VCS tags.

%files
%{py_sitedir}/*
%{_bindir}/poetry-dynamic-versioning
