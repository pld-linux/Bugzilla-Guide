Summary:	LDP Bugzilla Guide
Summary(pl):	Podrêcznik do Bugzilli
Name:		Bugzilla-Guide
Version:	2.14
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/bugzilla/%{name}.html.tar.gz
# Source0-md5:	634db96c1cfccdc2bca670de2e47ef00
URL:		http://www.tldp.org/LDP/bugzilla/Bugzilla-Guide/index.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is intended to be the comprehensive guide to the
installation, administration, maintenance, and use of the Bugzilla
bug-tracking system.

%description -l pl
Ten dokument ma byæ, w za³o¿eniach, wszechstronnym podrêcznikiem
instalacji, administracji, zarz±dzania i u¿ywania systemu ¶ledzenia
b³êdów Bugzilla.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

cp -ar * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
