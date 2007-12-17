%define name	nemiver
%define version	0.4.0
%define release %mkrel 1
%define major 0
%define lib_name %mklibname %{name} %{major}

Name: 	 	%{name}
Summary: 	Gtkmm front end to the GNU debugger
Version: 	%{version}
Release: 	%{release}

Source:		ftp://ftp.gnome.org/pub/GNOME/sources/nemiver/%{version}/%{name}-%{version}.tar.bz2
Source1:	%name.png
# (fc) 0.4.0-1mdv fix build with libgtop HEAD (SVN)
Patch0:		nemiver-0.4.0-libgtop.patch
URL:		http://home.gna.org/nemiver/
License:	GPL
Group:		Development/Other

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

Requires: gdb

Requires(post): desktop-file-utils 
Requires(postun): desktop-file-utils

%description
The nemiver project is an effort to develop a gtkmm front end to the
GNU debugger.

%package -n %{lib_name}
Summary:        Shared libraries for using nemiver
Group:          System/Libraries
Requires:       %{name} >= %{version}-%{release}
Provides:	libnemiver
Obsoletes:	libnemiver

%description -n %{lib_name}
Shared libraries for using nemiver

%package -n %{lib_name}-devel
Summary:        Shared libraries for using nemiver
Group:          Development/C++
Requires:       %{lib_name} >= %{version}-%{release}

%description -n %{lib_name}-devel
Shared libraries for using nemiver

%prep
%setup -q 
%patch0 -p1 -b .libgtop

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Nemiver" longtitle="Gtkmm front end to the GNU debugger" section="More Applications/Development/Tools" xdg="true"
EOF

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
rm -f %buildroot%_libdir/nemiver/*/*/*.a %buildroot%_libdir/nemiver/*/*.a %buildroot%_libdir/*.a

%find_lang %name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas %{name}-dbgperspective %{name}-workbench

%post -n %lib_name -p /sbin/ldconfig

%postun -n %lib_name -p /sbin/ldconfig

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
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_libdir}/%{name}
%dir %{_datadir}/omf/nemiver
%{_datadir}/omf/nemiver/*-C.omf
%lang(sv) %{_datadir}/omf/nemiver/*-sv.omf

%files -n %{lib_name}
%{_libdir}/*.so.%{major}*

%files -n %{lib_name}-devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}/*
%{_libdir}/*.la




