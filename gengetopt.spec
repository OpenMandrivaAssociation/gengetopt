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

%post
%_install_info %name.info

%postun
%_remove_install_info %name.info


%files
%defattr(-,root,root)
%doc installed-docs/*
%_bindir/gengetopt
%_datadir/gengetopt/
%_mandir/man1/gengetopt.1*
%_infodir/gengetopt.info*


