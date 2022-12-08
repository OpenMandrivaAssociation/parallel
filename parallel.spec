%global __requires_exclude /usr/bin/ksh|/bin/pdksh|/usr/bin/zsh|/usr/bin/fish|/bin/csh|/bin/tcsh|tcsh|mksh

Summary:	A shell tool for executing jobs in parallel
Name:		parallel
Version:	20221122
Release:	1
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
%doc %{_docdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%{_datadir}/bash-completion/completions/parallel
%{_datadir}/zsh/site-functions/_parallel
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*

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
