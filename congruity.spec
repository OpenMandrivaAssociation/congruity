Summary:	Logitech Harmony remote programmer GUI

Name:		congruity
Version:	18
Release:	1
License:	GPLv3+
URL:		http://congruity.sourceforge.net/
Source:		http://sourceforge.net/projects/congruity/files/congruity/18/%{name}-%{version}.tar.bz2
Group:		System/Configuration/Hardware
Requires:	python-libconcord
Requires:	wxPythonGTK
BuildArch:	noarch

%description
This software allows you to program your Logitech Harmony universal
remote.

%prep
%setup -q

%install
%makeinstall_std RUN_UPDATE_DESKTOP_DB=0 PREFIX=%{_prefix}

install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-harmony-www.desktop <<EOF
[Desktop Entry]
Name=Logitech Harmony configuration
Comment=Configure a Harmony remote
Exec=www-browser http://members.harmonyremote.com/
Type=Application
Icon=web_browser_section
Categories=Utility;Electronics;
StartupNotify=false
EOF

%files
%doc Changelog README.txt LICENSE.txt
%{_bindir}/congruity
%{_bindir}/mhgui
%{_datadir}/congruity
%{_datadir}/applications/congruity.desktop
%{_datadir}/applications/mandriva-harmony-www.desktop
%{_mandir}/man1/congruity*
%{_datadir}/applications/mhgui.desktop
%{_mandir}/man1/mhgui.1*



