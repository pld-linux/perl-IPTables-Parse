#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPTables
%define		pnam	Parse
Summary:	Perl interface to parse iptables rulesets
Name:		perl-IPTables-Parse
Version:	0.4
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cipherdyne.org/psad/download/psad-2.0.1.tar.gz
URL:		http://www.cipherdyne.org/psad/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
Perl interface to parse iptables rulesets.


%prep
%setup -q -n psad-2.0.1

%build
cd IPTables-Parse
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
cd IPTables-Parse
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc IPTables-Parse/{Changes,README}
%{_mandir}/man3/IPTables::Parse.3pm*
%{perl_vendorlib}/IPTables/Parse.pm
