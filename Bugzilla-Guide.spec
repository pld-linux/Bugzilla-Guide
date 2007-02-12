Summary:	LDP Bugzilla Guide
Summary(pl.UTF-8):	Podręcznik do Bugzilli
Name:		Bugzilla-Guide
Version:	2.14
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/bugzilla/%{name}.html.tar.gz
# Source0-md5:	634db96c1cfccdc2bca670de2e47ef00
URL:		http://www.tldp.org/LDP/bugzilla/Bugzilla-Guide/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is intended to be the comprehensive guide to the
installation, administration, maintenance, and use of the Bugzilla
bug-tracking system.

%description -l pl.UTF-8
Ten dokument ma być, w założeniach, wszechstronnym podręcznikiem
instalacji, administracji, zarządzania i używania systemu śledzenia
błędów Bugzilla.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
