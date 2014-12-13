Name:           clipgrab
Version:        3.4.8
Release:        3%{?dist}

License:        GPLv3 and Non-Commercial Use Only (Artwork and Trademark)
Group:          Applications/Internet
Summary:        A free video downloader and converter
URL:            http://clipgrab.de/en
Source0:        http://clipgrab.de/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop

BuildRequires:  qt-devel
BuildRequires:  qt-webkit-devel
BuildRequires:  desktop-file-utils
Requires:       ffmpeg


%description
ClipGrab is a free downloader and converter for YouTube, Vimeo, Dailymotion
and many other online video sites.

%prep
%setup -q -n %{name}
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
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/clipgrab.desktop


%changelog
* Sun Dec 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-3
- correct license field

* Sat Dec 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-2
- added  parallel make %%{?_smp_mflags} macro
- correct icon path in desktop file

* Sat Dec 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-1
- rebuild for new version
