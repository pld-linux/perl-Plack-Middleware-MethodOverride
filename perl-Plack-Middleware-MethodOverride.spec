#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Plack
%define		pnam	Middleware-MethodOverride
Summary:	Plack::Middleware-MethodOverride - Override REST methods to Plack apps via POST
Name:		perl-Plack-Middleware-MethodOverride
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3f2e8a64b59480a438983430a1b6ba2
URL:		https://metacpan.org/dist/Plack-Middleware-MethodOverride
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-Plack
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plack::Middleware::MethodOverride overrides the HTTP method of a
request, so that REST methods such as PUT or DELETE can be sent to
Plack applications via POST, using the X-HTTP-Method-Override header
or a query parameter.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Plack/Middleware/MethodOverride.pm
%{_mandir}/man3/*
