%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Graphical debugger intended for GNOME
Name:		nemiver
Version:	0.9.5
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://projects.gnome.org/nemiver/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/nemiver/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	dconf
BuildRequires:	gdb
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gdlmm-3.0) >= 3.0
BuildRequires:	pkgconfig(giomm-2.4) >= 2.15.2
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.14
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.14
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gsettings-desktop-schemas) >= 0.0.1
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.22
BuildRequires:	pkgconfig(gtkhex-3) >= 2.90
BuildRequires:	pkgconfig(gtkmm-3.0) >= 3.0
BuildRequires:	pkgconfig(gtksourceviewmm-3.0)
BuildRequires:	pkgconfig(gthread-2.0) >= 2.14
BuildRequires:	pkgconfig(libgtop-2.0) >= 2.14
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6.22
BuildRequires:	pkgconfig(sqlite3) >= 3.0
BuildRequires:	pkgconfig(vte-2.90) >= 0.28
Requires:	gdb

%description
Nemiver is a graphical debugger that integrates well in the GNOME
desktop environment. It currently features a backend which uses the
well known GNU Debugger gdb to debug C / C++ programs.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO* README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_iconsdir}/hicolor/*/apps/nemiver*
%{_iconsdir}/HighContrast/*/apps/nemiver*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

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

%find_lang %{name} --with-gnome

