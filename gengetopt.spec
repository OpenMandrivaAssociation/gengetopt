Summary:	Tool to write command line option parsing code for C/C++ programs
Name:		gengetopt
Version:	2.23
Release:	2
License:	GPLv2+
Group:		Development/Tools
URL:		https://www.gnu.org/software/gengetopt/gengetopt.html
Source0:	https://ftp.gnu.org/gnu/gengetopt/gengetopt-%{version}.tar.xz
BuildRequires:	gettext
BuildRequires:	bison flex
BuildRequires:	texinfo

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
%autosetup -p1
%configure

%build
%make_build

%install
%make_install
rm -rf %{buildroot}%{_infodir}/index.*

%files
%doc %{_docdir}/gengetopt
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/gengetopt
%{_infodir}/*.info*
