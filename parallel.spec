%define __noautoreq '/bin/csh|/usr/bin/fish|/usr/bin/ksh|/usr/bin/zsh|/bin/pdksh'

Summary:	A shell tool for executing jobs in parallel
Name:		parallel
Version:	20160522
Release:	5
License:	GPLv3+
Group:		File tools
Url:		http://www.gnu.org/software/parallel/
Source0:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2
Requires:	perl
BuildArch:	noarch

%description
GNU parallel is a shell tool for executing jobs in parallel locally
or using remote machines. A job is typically a single command or a small
script that has to be run for each of the lines in the input. The typical
input is a list of files, a list of hosts, a list of users, a list of URLs,
or a list of tables.

%files
%doc README NEWS
%doc %{_docdir}/%{name}
%{_bindir}/parallel
%{_bindir}/sem
%{_bindir}/sql
%{_bindir}/env_parallel*
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/sem.1*
%{_mandir}/man1/sql.1*
%{_bindir}/niceload
%config(noreplace) %{_sysconfdir}/%{name}/config
%{_mandir}/man1/env_parallel.1.*
%{_mandir}/man1/niceload.1*
%{_mandir}/man7/parallel_design.7.*
%{_mandir}/man7/parallel_tutorial.7.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# (Kharec: It seems we can have a site wide config file now, so create it directly at the install) 
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/config
