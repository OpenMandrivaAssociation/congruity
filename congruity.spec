
%define name	congruity
%define version	14
%define rel	1

Summary:	Logitech Harmony remote programmer GUI
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
# remote.png is CC-BY-SA, see LICENSE.txt:
License:	GPLv3+ and CC-BY-SA
URL:		http://congruity.sourceforge.net/
Source:		http://downloads.sourceforge.net/congruity/congruity-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
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
rm -rf %{buildroot}
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
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog README.txt LICENSE.txt
%{_bindir}/congruity
%{_datadir}/congruity
%{_datadir}/applications/congruity.desktop
%{_datadir}/applications/mandriva-harmony-www.desktop
%{_mandir}/man1/congruity*
