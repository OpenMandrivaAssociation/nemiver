Summary: 	Graphical debugger intended for GNOME
Name: 	 	nemiver
Version: 	0.9.3
Release: 	1
License:	GPLv2+
Group:		Development/Other
URL:		http://projects.gnome.org/nemiver/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/nemiver/%{name}-%{version}.tar.xz

BuildRequires: dconf
BuildRequires: gdb
BuildRequires: intltool
BuildRequires: boost-devel
BuildRequires: pkgconfig(gdlmm-3.0) >= 3.0
BuildRequires: pkgconfig(giomm-2.4) >= 2.15.2
BuildRequires: pkgconfig(glibmm-2.4) >= 2.14
BuildRequires: pkgconfig(gmodule-2.0) >= 2.14
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= 0.0.1
BuildRequires: pkgconfig(gthread-2.0) >= 2.14
BuildRequires: pkgconfig(gtk+-3.0) >= 2.22
BuildRequires: pkgconfig(gtkhex-3) >= 2.90
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.0
BuildRequires: pkgconfig(libgtop-2.0) >= 2.14
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.22
BuildRequires: pkgconfig(sqlite3) >= 3.0
BuildRequires: pkgconfig(vte-2.90) >= 0.28
BuildRequires: pkgconfig(gtksourceviewmm-3.0)
Requires:	gdb
Obsoletes:	%{_lib}nemiver0
Obsoletes:	%{_lib}nemiver0-devel

%description
Nemiver is a graphical debugger that integrates well in the GNOME
desktop environment. It currently features a backend which uses the
well known GNU Debugger gdb to debug C / C++ programs.

%prep
%setup -q 

%build
%configure2_5x \
	--enable-gsettings=yes \
	--disable-scrollkeeper \
	--disable-schemas-compile \
	--disable-schemas-install \
	--disable-static

%make

%install
%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_includedir}/* %{buildroot}%{_libdir}/pkgconfig

find %{buildroot} -name *.la -delete

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO* README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/nemiver*
%{_mandir}/man1/*



%changelog
* Mon Aug 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.3-1
+ Revision: 814444
- update to new version 0.9.3

* Sun May 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.2-1
+ Revision: 796924
- disable-scrollkeeper
- BR:pkgconfig(gtksourceviewmm-3.0) get back
- BR: pkgconfig(gtksourceviewmm-3.0) removed
- version update 0.9.2

* Sun May 08 2011 Götz Waschk <waschk@mandriva.org> 0.8.2-1
+ Revision: 672592
- new version
- update to new version 0.8.1

* Tue Oct 19 2010 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 586738
- new version

* Mon Dec 07 2009 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2010.1
+ Revision: 474345
- update to new version 0.7.3

* Sun Sep 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.2-1mdv2010.0
+ Revision: 438615
- update to new version 0.7.2

* Sat Aug 01 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.1-1mdv2010.0
+ Revision: 407277
- Update to new version 0.7.1

* Sat Jul 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 392363
- update to new version 0.7.0

* Wed Jun 10 2009 Götz Waschk <waschk@mandriva.org> 0.6.7-3mdv2010.0
+ Revision: 384701
- rebuild for new vte

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 0.6.7-2mdv2010.0
+ Revision: 382170
- rebuild for new libvte

* Mon May 04 2009 Götz Waschk <waschk@mandriva.org> 0.6.7-1mdv2010.0
+ Revision: 371601
- update to new version 0.6.7

* Mon Apr 06 2009 Frederic Crozat <fcrozat@mandriva.com> 0.6.6-1mdv2009.1
+ Revision: 364441
- Release 0.6.6

* Wed Mar 11 2009 Frederic Crozat <fcrozat@mandriva.com> 0.6.5-3mdv2009.1
+ Revision: 353821
- Patch0 (GIT): update ephy-spinner

* Mon Mar 02 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.5-2mdv2009.1
+ Revision: 347261
- obsoletes old and uneeded libraries

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 0.6.5-1mdv2009.1
+ Revision: 346896
- update build deps
- update to new version 0.6.5
- fix source URL

  + Funda Wang <fwang@mandriva.org>
    - update url

* Thu Nov 27 2008 Funda Wang <fwang@mandriva.org> 0.6.4-1mdv2009.1
+ Revision: 307223
- new version 0.6.4

* Tue Nov 11 2008 Funda Wang <fwang@mandriva.org> 0.6.3-3mdv2009.1
+ Revision: 302016
- rebuild for xcb
- add debugger category

* Sat Oct 11 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.3-1mdv2009.1
+ Revision: 292588
- drop old Mandriva menu category from .desktop file
- new release 0.6.3

* Sat Aug 30 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.2-1mdv2009.0
+ Revision: 277620
- Release 0.6.2

* Thu Jul 31 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.1-1mdv2009.0
+ Revision: 257953
- Release 0.6.1

* Mon Jun 23 2008 Frederic Crozat <fcrozat@mandriva.com> 0.5.4-1mdv2009.0
+ Revision: 227991
- Release 0.5.4

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue May 27 2008 Funda Wang <fwang@mandriva.org> 0.5.3-1mdv2009.0
+ Revision: 211507
- New version 0.5.3

* Tue May 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.5.2-1mdv2009.0
+ Revision: 206523
- new release 0.5.2
- drop unneeded old icon locations
- spec clean

* Tue Mar 18 2008 Michael Scherer <misc@mandriva.org> 0.5.0-2mdv2008.1
+ Revision: 188535
- fix buildrequires
- add support for memoryview option, as pointed by dodji on #gnome-fr

* Sun Mar 16 2008 Frederic Crozat <fcrozat@mandriva.com> 0.5.0-1mdv2008.1
+ Revision: 188179
- Release 0.5.0

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 03 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1mdv2008.0
+ Revision: 58512
-Patch0: fix build with recent libgtop
-fix buildrequires

  + Jérôme Soyer <saispo@mandriva.org>
    - Add BuildRequires
    - New release 0.4.0


* Sun Jan 21 2007 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2007.0
+ Revision: 111404
- new version
- bump deps
- update file list
- fix split between main and library package

* Fri Dec 15 2006 Jérôme Soyer <saispo@mandriva.org> 0.2.0-4mdv2007.1
+ Revision: 97291
- Fix sqlite
- Fix Release
- Fix sqlite

* Fri Dec 15 2006 Jérôme Soyer <saispo@mandriva.org> 0.2.0-3mdv2007.1
+ Revision: 97229
- Fix exclude
- Fix bug
- Fix bug
- Fix bug
- Fix preun
- Fix schemas and Requires

* Thu Dec 14 2006 Jérôme Soyer <saispo@mandriva.org> 0.2.0-1mdv2007.1
+ Revision: 96802
- New release 0.2.0

* Mon Dec 11 2006 Jérôme Soyer <saispo@mandriva.org> 0.1.0-2mdv2007.1
+ Revision: 94681
- Repush
- Repush
- Add BuildRequires
- Add BuildRequires
- Add BuildRequires
- Fix BuildRequires
- Add BuildRequires
- Fix
- Add BuildRequires
- Add BuildRequires
- Import nemiver

* Mon Nov 27 2006 Jerome Soyer <saispo@mandriva.org> 0.1.0-1mdv2007.0
- First release

