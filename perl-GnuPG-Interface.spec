%define upstream_name	 GnuPG-Interface
%define upstream_version 0.50
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	GnuPG-Interface module for perl

Group:		Development/Perl
License:	GPL
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GnuPG/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	gnupg
BuildRequires: perl(strictures)
BuildRequires: perl(Moo)
BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Class::MethodMaker)
# For interactive tests
BuildRequires:	perl(Expect)

Requires:	perl(Class::MethodMaker)
BuildArch:	noarch


%description
GnuPG::Interface and its associated modules
are designed to provide an object-oriented
method for interacting with GnuPG, being able
to perform functions such as but not limited
to encrypting, signing, decryption, verification,
and key-listing parsing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
perl -mExpect -e 'my $e=Expect->spawn("make test");
$e->expect(undef);
exit $e->exitstatus()'

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/GnuPG
%{_mandir}/*/*


