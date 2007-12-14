# TODO:
# - drop bluez-libs-devel and other not needed stuff
%define		module	ssl
Summary:	SSL wrapper for socket objects from Python 2.6
Name:		python-%{module}
Version:	1.13
Release:	0.1
License:	PSF
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/s/ssl/ssl-%{version}.tar.gz
# Source0-md5:	f254773cb8023379fd071fd51112189a
URL:		http://docs.python.org/dev/library/ssl.html
BuildRequires:	bluez-libs-devel
BuildRequires:	krb5-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	python-devel < 1:2.6
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The old socket.ssl() support for TLS over sockets is being superseded
in Python 2.6 by a new 'ssl' module. This package brings that module
to older Python releases, 2.3.5 and up (it may also work on older
versions of 2.3, but we haven't tried it).

It's quite similar to the 2.6 ssl module. The only significant
difference is that the ssl.SSLError exception does not inherit from
socket.error, as it does in Python 2.6, because socket.error is not
exposed at the C level in Python 2.3.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/ssl
%attr(755,root,root) %{py_sitedir}/ssl/*.so
%{py_sitedir}/ssl/*.py[oc]
%{py_sitedir}/*.egg-info
