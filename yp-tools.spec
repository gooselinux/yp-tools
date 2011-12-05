Summary: NIS (or YP) client programs
Name: yp-tools
Version: 2.9
Release: 10%{?dist}
License: GPLv2
Group: System Environment/Base
Source: ftp://ftp.kernel.org/pub/linux/utils/net/NIS/yp-tools-%{version}.tar.bz2
Url: http://www.linux-nis.org/nis/yp-tools/index.html
Patch1: yp-tools-2.7-md5.patch
# rhbz#487607
Patch2: yp-tools-2.9-sha-2.patch
Requires: ypbind
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The Network Information Service (NIS) is a system which provides
network information (login names, passwords, home directories, group
information) to all of the machines on a network.  NIS can enable
users to login on any machine on the network, as long as the machine
has the NIS client programs running and the user's password is
recorded in the NIS passwd database.  NIS was formerly known as Sun
Yellow Pages (YP).

This package's NIS implementation is based on FreeBSD's YP and is a
special port for glibc 2.x and libc versions 5.4.21 and later.  This
package only provides the NIS client programs.  In order to use the
clients, you'll need to already have an NIS server running on your
network. An NIS server is provided in the ypserv package.

Install the yp-tools package if you need NIS client programs for machines
on your network.  You will also need to install the ypbind package on
every machine running NIS client programs.  If you need an NIS server,
you'll need to install the ypserv package on one machine on the network.

%prep
%setup -q
%patch1 -p1 -b .md5
%patch2 -p1 -b .sha-2

%build
%configure --disable-domainname
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" INSTALL_PROGRAM=install install

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog NEWS etc/nsswitch.conf
%doc THANKS TODO
/usr/bin/*
%{_mandir}/*/*
/usr/sbin/*
/var/yp/nicknames
%dir /var/yp

%changelog
* Thu May 13 2010 Karel Klic <kklic@redhat.com> - 2.9-10
- Rebuild to generate correct dwarf cfi data
  Resolves: #589920

* Fri Feb 26 2010 Karel Klic <kklic@redhat.com> - 2.9-9
- Removed dot at the end of the summary
- Removed Obsoletes: yppasswd, yp-clients

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.9-8.1
- Rebuilt for RHEL 6

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.9-8
- Convert specfile to UTF-8.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar  4 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.9-6
- Add SHA-2 password hashes support
  Resolves: #487607

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.9-4
- Fix license tag.

* Mon Feb 11 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.9-3
- Fix Buildroot

* Tue Jul 31 2007 Steve Dickson <steved@redhat.com> 2.9-1
- Changed install process to create an useful debuginfo package (bz 249961) 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.9-0.1
- rebuild

* Mon Feb 13 2006 Chris Feist <cfeist@redhat.com> - 2.9-0
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.8-8.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Jun 18 2004 Alan Cox <alan@redhat.com>
- Fix buffer overflow (non security) thanks to D Binderman

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 23 2003 Steve Dickson <SteveD@RedHat.com>
- Update to 2.7 from upstream
- Updated yppasswd md5 patch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Wed Aug 28 2002 Nalin Dahyabhai <nalin@redhat.com> 2.7-3
- properly terminate an alloca'ed string in yppasswd which would lead to
  improper rejection of the request if the user's pw_passwd was visible

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Alexander Larsson <alexl@redhat.com>
- Update to 2.7 from upstream
- Updated yppasswd md5 patch

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar 25 2002 Alex Larsson <alexl@redhat.com> 2.6-4
- Updated passwd patch with Nalins comments

* Fri Mar 22 2002 Alex Larsson <alexl@redhat.com> 2.6-3
- Add patch that handles MD5 passwords and HPU/X password aging.
- This should hopefully fix #19045 and #22667

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jul 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- own /var/yp

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Feb 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify

* Wed Sep 27 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add another security patch

* Sun Aug 20 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- allow passwords up to 128 characters

* Tue Aug 15 2000 Nalin Dahyabhai <nalin@redhat.com>
- change License from GNU to GPL
- fix handling of defaults in ypchfn (#13830)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- use %%{_mandir}

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- man pages are compressed
- version 2.4

* Tue Oct 26 1999 Bill Nottingham <notting@redhat.com>
- get rid of bogus messages.

* Fri Aug 27 1999 Preston Brown <pbrown@redhat.com>
- patched /var/yp/nicknames so that hosts resolves to hosts.byname,
- not hosts.byaddr (bug # 2389)

* Sun May 30 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.3.

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- version 2.2
- make it obsolete older yp-clients package

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2/1
- version 2.1
- require ypbind

* Fri Jun 12 1998 Aron Griffis <agriffis@coat.com>
- upgraded to 2.0

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Apr 13 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.4.1

* Thu Dec 04 1997 Cristian Gafton <gafton@redhat.com>
- put yppasswd again in the package, 'cause it is the right thing to do
  (sorry djb!)
- obsoletes old, unmaintained yppasswd package

* Sat Nov 01 1997 Donnie Barnes <djb@redhat.com>
- removed yppasswd from this package.

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>
- pulled from contrib into distribution (got fresh sources).  Thanks
  to Thorsten Kukuk <kukuk@vt.uni-paderborn.de> for the original.
- used fresh sources
