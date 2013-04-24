%define name gengetopt
%define version 2.22.5
%define release %mkrel 1

Summary: GNU gengetopt generates command line parsers
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.gz
License: GPL
Group: Development/C
URL: http://www.gnu.org/software/gengetopt/gengetopt.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: flex

%description
This program generates a C function that uses getopt_long function to parse
the command line options, to validate them and fills a struct.

Thus your program can now handle options such as:

myprog --input foo.c -o foo.o --no-tabs -i 100 *.class

And both long options (those that start with --) and short options (start
with - and consist of only one character) can be handled. For standards
about short and long options you may want to take a look at the GNU Coding
Standards.

%prep
%setup -q

%build
%configure2_5x
#gw parallel build is broken
make

%check
%make check

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
mv %buildroot/%_datadir/doc/gengetopt installed-docs

%clean
rm -rf $RPM_BUILD_ROOT




%files
%defattr(-,root,root)
%doc installed-docs/*
%_bindir/gengetopt
%_datadir/gengetopt/
%_mandir/man1/gengetopt.1*
%_infodir/gengetopt.info*




%changelog
* Mon Sep 26 2011 Götz Waschk <waschk@mandriva.org> 2.22.5-1mdv2012.0
+ Revision: 701245
- new version

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.22.4-2mdv2011.0
+ Revision: 610828
- rebuild

* Wed Dec 23 2009 Götz Waschk <waschk@mandriva.org> 2.22.4-1mdv2010.1
+ Revision: 481911
- update to new version 2.22.4

* Thu Oct 01 2009 Götz Waschk <waschk@mandriva.org> 2.22.3-1mdv2010.0
+ Revision: 452161
- update to new version 2.22.3

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 2.22.2-1mdv2010.0
+ Revision: 385859
- new version 2.22.2

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.22.1-2mdv2009.0
+ Revision: 266841
- rebuild early 2009.0 package (before pixel changes)

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Tue Jan 15 2008 Götz Waschk <waschk@mandriva.org> 2.22-1mdv2008.1
+ Revision: 152024
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 07 2007 Götz Waschk <waschk@mandriva.org> 2.21-1mdv2008.0
+ Revision: 59665
- new version

* Thu Jul 05 2007 Götz Waschk <waschk@mandriva.org> 2.20-1mdv2008.0
+ Revision: 48681
- new version


* Thu Jan 18 2007 Götz Waschk <waschk@mandriva.org> 2.19.1-1mdv2007.0
+ Revision: 110309
- new version
- add check

* Tue Jan 02 2007 Götz Waschk <waschk@mandriva.org> 2.19-1mdv2007.1
+ Revision: 103483
- new version
- Import gengetopt

* Tue Sep 26 2006 Götz Waschk <waschk@mandriva.org> 2.18-1mdv2007.0
- New version 2.18

* Sun Jul 23 2006 Götz Waschk <waschk@mandriva.org> 2.17-1mdv2007.0
- New release 2.17

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 2.16-2mdk
- Rebuild

* Tue Mar 07 2006 Götz Waschk <waschk@mandriva.org> 2.16-1mdk
- New release 2.16

* Wed Dec 28 2005 Götz Waschk <waschk@mandriva.org> 2.15-1mdk
- New release 2.15
- use mkrel

* Tue Sep 06 2005 Götz Waschk <waschk@mandriva.org> 2.14-1mdk
- New release 2.14

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 2.13.1-1mdk
- New release 2.13.1

* Tue Dec 21 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.13-1mdk
- fix doc file listing
- New release 2.13

* Tue Aug 24 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.12.2-1mdk
- new version

* Wed Jun 16 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.12.1-2mdk
- rebuild for new g++

* Thu Apr 22 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.12.1-1mdk
- fix source URL
- new version

