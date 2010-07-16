Name:		parallel
Summary:	A shell tool for executing jobs in parallel
Version:	20100620
Release:	%mkrel 1
License:	GPLv3
Source0:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2
Source1:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2.sig
URL:		http://www.gnu.org/software/parallel/
Group:		File tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
GNU parallel is a shell tool for executing jobs in parallel locally or using remote machines. A job is typically a singlecommand or a small script that has to be run for each of the lines in the input. The typical input is a list of files, alist of hosts, a list of users, a list of URLs, or a list of tables.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root) 
%doc README NEWS 
%{_bindir}/parallel
%{_datadir}/doc/parallel/parallel.html
%{_mandir}/man1/parallel.1.lzma
