Summary:	GNU gengetopt generates command line parsers
Name:		gengetopt
Version:	2.22.6
Release:	1
License:	GPLv3+
Group:		Development/C
Url:		http://www.gnu.org/software/gengetopt/gengetopt.html
Source0:	ftp://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	bison
BuildRequires:	flex

%description
This program generates a C function that uses getopt_long function to parse
the command line options, to validate them and fills a struct.

Thus your program can now handle options such as:

myprog --input foo.c -o foo.o --no-tabs -i 100 *.class

And both long options (those that start with --) and short options (start
with - and consist of only one character) can be handled. For standards
about short and long options you may want to take a look at the GNU Coding
Standards.

%files
%doc %{_docdir}/%{name}/*
%{_bindir}/gengetopt
%{_datadir}/gengetopt/
%{_mandir}/man1/gengetopt.1*
%{_infodir}/gengetopt.info*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
make

%check
%make check

%install
%makeinstall_std

