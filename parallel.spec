Name:		parallel
Summary:	A shell tool for executing jobs in parallel
Version:	20120622
Release:	%mkrel 1
License:	GPLv3+
Source0:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2
Source1:	http://ftp.gnu.org/gnu/parallel/%{name}-%{version}.tar.bz2.sig
URL:		http://www.gnu.org/software/parallel/
Group:		File tools
Requires:	perl
BuildArch:	noarch

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
%defattr(-,root,root)
%doc README NEWS
%{_bindir}/parallel
%{_bindir}/sem
%{_bindir}/sql
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/sem.1*
%{_mandir}/man1/sql.1*
%{_bindir}/niceload
%config(noreplace) %{_sysconfdir}/%{name}/config
%{_mandir}/man1/niceload.1*


%changelog
* Fri Jun 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20120622-1mdv2012.0
+ Revision: 807513
- update to 20120622

* Fri May 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20120522-1
+ Revision: 800734
- update to 20120522

* Sun Apr 22 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20120422-1
+ Revision: 792727
- update to 20120422

* Thu Mar 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20120322-1
+ Revision: 788195
- new version 20120322

* Thu Feb 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20120222-1
+ Revision: 779343
- update to 20120122

* Wed Feb 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20120122-1
+ Revision: 770454
- update to 20120122
- noarch

* Sun Nov 27 2011 Andrey Bondrov <abondrov@mandriva.org> 20111122-1
+ Revision: 733734
- New version 20111122

* Wed Jun 22 2011 Götz Waschk <waschk@mandriva.org> 20110622-1
+ Revision: 686607
- update to new version 20110622

* Sun May 22 2011 Götz Waschk <waschk@mandriva.org> 20110522-1
+ Revision: 677260
- update to new version 20110522

* Fri Apr 22 2011 Sandro Cazzaniga <kharec@mandriva.org> 20110422-1
+ Revision: 656734
- new version 20110422

* Tue Mar 22 2011 Sandro Cazzaniga <kharec@mandriva.org> 20110322-1
+ Revision: 647482
- new version 20110322
- create the config file (This should solve the issue with some packagers renaming GNU Parallel to gparallel to avoid the naming conflict)

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 20110205-2
+ Revision: 643879
- rebuild to obsolete old packages

* Tue Feb 08 2011 Sandro Cazzaniga <kharec@mandriva.org> 20110205-1
+ Revision: 636784
- update to 20110205

* Sat Jan 29 2011 Sandro Cazzaniga <kharec@mandriva.org> 20110125-1
+ Revision: 633837
- Really update to 20110125

* Sat Jan 22 2011 Sandro Cazzaniga <kharec@mandriva.org> 20101222-1
+ Revision: 632217
- new version 20101222

* Sun Dec 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 20101202-1mdv2011.0
+ Revision: 610659
- update to 20101202

* Sat Nov 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 20101122-1mdv2011.0
+ Revision: 601751
- update to new version
- update file list

* Sat Oct 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100922-1mdv2011.0
+ Revision: 584331
- new version

* Wed Sep 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100906-1mdv2011.0
+ Revision: 576811
- update to 20100906
- update file list

* Mon Aug 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100822-1mdv2011.0
+ Revision: 572129
- don't use %%make anymore
- new version 20100822
- update file list

* Thu Jul 29 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-3mdv2011.0
+ Revision: 563194
- fix summary with "shell tool", recommended by upstream.
- fix summary (thanks Samuel Verschelde)

* Sat Jul 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-1mdv2011.0
+ Revision: 557949
- fix description (it's a perl tool!)
- update to 20100722

  + Jani Välimaa <wally@mandriva.org>
    - split one-liner description to a multiple lines
    - fix one file appearing twice in file list

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-2mdv2011.0
+ Revision: 554151
- Add Require

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-1mdv2011.0
+ Revision: 554150
- import parallel


