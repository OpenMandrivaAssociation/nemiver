%define name	nemiver
%define version	0.6.4
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Graphical debugger intended for GNOME
Version: 	%{version}
Release: 	%{release}
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/nemiver/0.6/%{name}-%{version}.tar.bz2
URL:		http://home.gna.org/nemiver/
License:	GPLv2+
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	libglademm-devel
BuildRequires:	libgtksourceviewmm-devel >= 0.3.0
BuildRequires:	libgnome2-devel
BuildRequires:	libvte-devel
BuildRequires:	gconfmm2.6-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	sqlite3-devel
BuildRequires:	gdb
BuildRequires:	boost-devel
BuildRequires:	libgtop2.0-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libsm-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	libgtkhex-devel 
Requires:	gdb

Requires(post):		desktop-file-utils 
Requires(postun):	desktop-file-utils

%description
Nemiver is a graphical debugger that integrates well in the GNOME
desktop environment. It currently features a backend which uses the
well known GNU Debugger gdb to debug C / C++ programs.

%prep
%setup -q 

%build
%configure2_5x 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#menu

desktop-file-install --vendor="" \
  --add-category="Debugger" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#remove unpackaged files
rm -rf %{buildroot}%{_includedir}/* %{buildroot}%{_libdir}/pkgconfig
rm -f %{buildroot}%{_libdir}/nemiver/*/*/*.{a,la} %{buildroot}%{_libdir}/nemiver/*/*.{a,la} %{buildroot}%{_libdir}/nemiver/*.{la,a}

%find_lang %{name} --with-gnome

%clean
rm -rf %{buildroot}

%define schemas %{name}-dbgperspective %{name}-workbench

%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas %{schemas}
%update_icon_cache hicolor
%update_scrollkeeper
%endif

%preun
%preun_uninstall_gconf_schemas %{schemas}

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%clean_scrollkeeper
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO* README
%{_sysconfdir}/gconf/schemas/%{name}-dbgperspective.schemas
%{_sysconfdir}/gconf/schemas/%{name}-workbench.schemas
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/nemiver*
%{_libdir}/%{name}
%{_mandir}/man1/*
%dir %{_datadir}/omf/nemiver
%{_datadir}/omf/nemiver/*-C.omf
%lang(sv) %{_datadir}/omf/nemiver/*-sv.omf
%lang(es) %{_datadir}/omf/nemiver/*-es.omf
%lang(oc) %{_datadir}/omf/nemiver/*-oc.omf

