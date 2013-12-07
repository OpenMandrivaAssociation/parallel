Summary:	A shell tool for executing jobs in parallel
Name:		parallel
Version:	20121122
Release:	5
License:	GPLv3+
Group:		File tools
Url:		http://www.gnu.org/software/parallel/
Source0:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2
Source1:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2.sig
BuildArch:	noarch
Requires:	perl

%description
GNU parallel is a shell tool for executing jobs in parallel locally
or using remote machines. A job is typically a single command or a small
script that has to be run for each of the lines in the input. The typical
input is a list of files, a list of hosts, a list of users, a list of URLs,
or a list of tables.

%prep
%setup -q

%build
%configure2_5x
make

%install
%makeinstall_std

# (Kharec: It seems we can have a site wide config file now, so create it directly at the install) 
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/config

%files
%doc README NEWS
%config(noreplace) %{_sysconfdir}/%{name}/config
%{_bindir}/parallel
%{_bindir}/sem
%{_bindir}/sql
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/sem.1*
%{_mandir}/man1/sql.1*
%{_bindir}/niceload
%{_mandir}/man1/niceload.1*

