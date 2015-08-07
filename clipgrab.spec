Name:           clipgrab
Version:        3.5.1
Release:        1%{?dist}

License:        GPLv3 and Non-Commercial Use Only (Artwork and Trademark)
Group:          Applications/Internet
Summary:        A free video downloader and converter
URL:            http://clipgrab.de/en
Source0:        http://clipgrab.de/download/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  qt-devel
BuildRequires:  qt-webkit-devel
BuildRequires:  desktop-file-utils
Requires:       ffmpeg


%description
ClipGrab is a free downloader and converter for YouTube, Vimeo, Dailymotion
and many other online video sites.

%prep
%setup -q -n %{name}-%{version}
chmod 0644 *.cpp *.h icon.png COPYING README license.odt

%build
qmake-qt4 %{name}.pro
make %{?_smp_mflags}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
install -Dm 644 icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/clipgrab.desktop


%changelog
* Fri Aug 07 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1

* Fri May 22 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.4.11-1
- Update to 3.4.11

* Tue Feb 03 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.4.9-1
- Update to 3.4.9
- Mark license files as %%license where available

* Sun Dec 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-3
- correct license field

* Sat Dec 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-2
- added  parallel make %%{?_smp_mflags} macro
- correct icon path in desktop file

* Sat Dec 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-1
- rebuild for new version
