#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	IPTables
%define		pnam	Parse
Summary:	Perl interface to parse iptables rulesets
Summary(pl.UTF-8):	Perlowy interfejs do analizy zbiorów reguł iptables
Name:		perl-IPTables-Parse
Version:	0.4
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cipherdyne.org/psad/download/psad-2.0.1.tar.gz
# Source0-md5:	a1604b68e31178e7e0cbbfd7c1cd4edf
Patch0:		%{name}-iptables.patch
URL:		http://www.cipherdyne.org/psad/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to parse iptables rulesets.

%description -l pl.UTF-8
Perlowy interfejs do analizy zbiorów reguł iptables.

%prep
%setup -q -n psad-2.0.1
%patch0 -p1

%build
cd IPTables-Parse
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C IPTables-Parse pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc IPTables-Parse/{Changes,README}
%{_mandir}/man3/IPTables::Parse.3pm*
%dir %{perl_vendorlib}/IPTables
%{perl_vendorlib}/IPTables/Parse.pm
