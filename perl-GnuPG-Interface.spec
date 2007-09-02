%define module	GnuPG-Interface
%define name	perl-%{module}
%define version 0.36
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	GnuPG-Interface module for perl
Group:		Development/Perl
License:	GPL
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/GnuPG/%{module}-%{version}.tar.gz
BuildRequires:	perl(Class::MethodMaker)
BuildRequires:  gnupg
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GnuPG::Interface and its associated modules
are designed to provide an object-oriented
method for interacting with GnuPG, being able
to perform functions such as but not limited
to encrypting, signing, decryption, verification,
and key-listing parsing.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/GnuPG
%{perl_vendorlib}/auto/GnuPG
%{_mandir}/*/*

