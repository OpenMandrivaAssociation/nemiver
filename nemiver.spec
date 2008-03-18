%define name	nemiver
%define version	0.5.0
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Gtkmm front end to the GNU debugger
Version: 	%{version}
Release: 	%{release}

Source:		ftp://ftp.gnome.org/pub/GNOME/sources/nemiver/%{version}/%{name}-%{version}.tar.bz2
Source1:	%name.png
URL:		http://home.gna.org/nemiver/
License:	GPL
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires: libglademm-devel
BuildRequires: libgtksourceviewmm-devel >= 0.3.0
BuildRequires: libgnome2-devel
BuildRequires: libvte-devel
BuildRequires: gconfmm2.6-devel
BuildRequires: gnome-vfs2-devel
BuildRequires: sqlite3-devel
BuildRequires: gdb
BuildRequires: boost-devel
BuildRequires: libgtop2.0-devel
BuildRequires: desktop-file-utils
BuildRequires: libsm-devel
BuildRequires: ImageMagick
BuildRequires: gnome-doc-utils
BuildRequires: libgtkhex-devel 
Requires: gdb

Requires(post): desktop-file-utils 
Requires(postun): desktop-file-utils

%description
The nemiver project is an effort to develop a gtkmm front end to the
GNU debugger.

%prep
%setup -q 

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
   --remove-category="" \
  --add-category="X-MandrivaLinux-MoreApplications-Development-Tools;" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %SOURCE1 $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %SOURCE1 $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %SOURCE1 $RPM_BUILD_ROOT/%_miconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
cp %SOURCE1 $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/
cp %SOURCE1 $RPM_BUILD_ROOT/%{_datadir}/icons/

#remove unpackaged files
rm -rf %buildroot%_includedir/* %buildroot%_libdir/pkgconfig
rm -f %buildroot%_libdir/nemiver/*/*/*.{a,la} %buildroot%_libdir/nemiver/*/*.{a,la} %buildroot%_libdir/nemiver/*.{la,a}

%find_lang %name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas %{name}-dbgperspective %{name}-workbench

%post
%update_menus
%post_install_gconf_schemas %{schemas}
%update_icon_cache hicolor
%update_scrollkeeper

%preun
%preun_uninstall_gconf_schemas %{schemas}

%postun
%clean_menus
%clean_icon_cache hicolor
%clean_scrollkeeper

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO* README
%{_sysconfdir}/gconf/schemas/%{name}-dbgperspective.schemas
%{_sysconfdir}/gconf/schemas/%{name}-workbench.schemas
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/nemiver*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_libdir}/%{name}
%{_mandir}/man1/*
%dir %{_datadir}/omf/nemiver
%{_datadir}/omf/nemiver/*-C.omf
%lang(sv) %{_datadir}/omf/nemiver/*-sv.omf
%lang(es) %{_datadir}/omf/nemiver/*-es.omf
%lang(oc) %{_datadir}/omf/nemiver/*-oc.omf

