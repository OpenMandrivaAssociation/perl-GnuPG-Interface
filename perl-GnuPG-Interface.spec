%define upstream_name	 GnuPG-Interface
%define upstream_version 0.46
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.46
Release:	3

Summary:	GnuPG-Interface module for perl
Group:		Development/Perl
License:	GPL
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GnuPG/GnuPG-Interface-0.46.tar.gz

BuildRequires:	gnupg
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

%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.440.0-1mdv2011.0
+ Revision: 672849
- update to new version 0.44

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.430.0-1
+ Revision: 643380
- update to new version 0.43

* Thu Oct 01 2009 Pascal Terjan <pterjan@mandriva.org> 0.420.0-2mdv2011.0
+ Revision: 452089
- Actually run the tests

* Thu Oct 01 2009 Pascal Terjan <pterjan@mandriva.org> 0.420.0-1mdv2010.0
+ Revision: 452088
- Allow interactives tests to run, using Expect

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - adding missing buildrequires:
    - update to 0.42

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 407753
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.36-4mdv2009.0
+ Revision: 257126
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-2mdv2008.1
+ Revision: 107247
- add missing dependency

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2008.0
+ Revision: 78440
- new version

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 0.35-1mdv2008.0
+ Revision: 19147
- 0.35


* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.33-9mdk
- Fix Buildrequires

* Fri Aug 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-8mdk
- spec cleanup 
- source url
- better url
- make test in %%check
- fix tests

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.33-7mdk 
- really fix buildrequires
- remove MANIFEST
- spec cleanup

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.33-6mdk
- fix buildrequires in a backward compatible way

* Wed Feb 11 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.33-5mdk
- Own dir

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.33-4mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- rm -rf /tmp/perl-GnuPG-Interface-0.33 in %%install, not %%prep
- use %%makeinstall_std macro

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.33-3mdk
- rebuild for new auto{prov,req}

* Fri Jan 24 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.33-2mdk
- rebuilt

* Thu Jul 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.33-1mdk
- 0.33

* Fri Mar 08 2002 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.31-2mdk
- First MandrakeSoft Package.


