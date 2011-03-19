%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%global srcname apipkg

Name:           python-%{srcname}
Version:        1.0
Release:        1%{?dist}
Summary:        Python namespace control and lazy-import mechanism

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/apipkg
Source0:        http://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose


%description
With apipkg you can control the exported namespace of a python package and
greatly reduce the number of imports for your users. It is a small python
module that works on virtually all Python versions, including CPython2.3 to
Python3.1, Jython and PyPy. It co-operates well with Python's help() system,
custom importers (PEP302) and common command line completion tools.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGELOG README.txt
%{python_sitelib}/%{srcname}.p*
%{python_sitelib}/%{srcname}*.egg-info


%changelog
* Wed Nov 08 2010 Fabian Affolter <fabian@bernewireless.net> - 1.0-1
- Initial package
