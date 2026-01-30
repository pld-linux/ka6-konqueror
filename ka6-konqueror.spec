#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.12.1
%define		kframever	5.240.0
%define		qtver		6.4.0
%define		kaname		konqueror
Summary:	konqueror
Name:		ka6-%{kaname}
Version:	25.12.1
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	fc6d7b6ec8c3cb94693b83c8fbfd33cb
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
%{?with_tests:BuildRequires:	Qt6Test-devel >= %{qtver}}
BuildRequires:	Qt6TextToSpeech-devel >= %{qtver}
BuildRequires:	Qt6WebEngine-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-tools
BuildRequires:	hunspell-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-karchive-devel >= %{kframever}
BuildRequires:	kf6-kbookmarks-devel >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdesu-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kguiaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwallet-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-sonnet-devel >= %{kframever}
BuildRequires:	kp6-plasma-activities-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-data = %{version}-%{release}
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
ExclusiveArch:	%{x8664} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konqueror is KDE's Webbrowser and swiss-army-knife for any kind of
file-management and file previewing.. Features. Webbrowsing using
KHTML or KDEWebKit as rendering engines; File management using most of
Dolphin's features (including version-control, service menus and the
basic UI)

%description -l pl.UTF-8
Konqueror jest przeglądarką www KDE i szwajcarskim scyzorykiem do
każdego rodzaju zarządzania plikami i ich podglądem. Cechy:
przeglądanie www przy użyciu KHTML lub KDEWebKit jako silników
renderowania; zarządzanie plikami używając większości możliwości
Dolphina (łącznie z kontrolą wersji, menu i podstawowym UI).

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
Obsoletes:	ka5-%{kaname}-data < %{version}
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{el,ko,sr,zh_CN}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
/etc/xdg/autostart/konqy_preload.desktop
/etc/xdg/konqautofiltersrc
/etc/xdg/konqsidebartngrc
/etc/xdg/translaterc
/etc/xdg/useragenttemplatesrc
%attr(755,root,root) %{_bindir}/fsview
%attr(755,root,root) %{_bindir}/kcreatewebarchive
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%{_libdir}/libKF6Konq.so.*.*
%{_libdir}/libKF6Konq.so.7
%{_libdir}/libkonqsidebarplugin.so.*.*
%{_libdir}/libkonqsidebarplugin.so.6
%{_libdir}/libkonquerorprivate.so.*.*
%{_libdir}/libkonquerorprivate.so.5
%{_libdir}/qt6/plugins/akregatorkonqfeedicon.so
%{_libdir}/qt6/plugins/autorefresh.so
%{_libdir}/qt6/plugins/babelfishplugin.so
%dir %{_libdir}/qt6/plugins/dolphinpart
%dir %{_libdir}/qt6/plugins/dolphinpart/kpartplugins
%{_libdir}/qt6/plugins/dolphinpart/kpartplugins/dirfilterplugin.so
%{_libdir}/qt6/plugins/dolphinpart/kpartplugins/kimgallery.so
%{_libdir}/qt6/plugins/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%{_libdir}/qt6/plugins/kf6/kfileitemaction/akregatorplugin.so
%{_libdir}/qt6/plugins/kf6/kio/bookmarks.so
%{_libdir}/qt6/plugins/kf6/parts/fsviewpart.so
%{_libdir}/qt6/plugins/kf6/parts/konq_sidebar.so
%{_libdir}/qt6/plugins/kf6/parts/webenginepart.so
%{_libdir}/qt6/plugins/khtmlsettingsplugin.so
%dir %{_libdir}/qt6/plugins/konqueror
%dir %{_libdir}/qt6/plugins/konqueror/kpartplugins
%dir %{_libdir}/qt6/plugins/konqueror/sidebar
%{_libdir}/qt6/plugins/konqueror/kpartplugins/searchbarplugin.so
%{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_bookmarks.so
%{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_history.so
%{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_places.so
%{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_tree.so
%{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_verticaltabbar.so
%dir %{_libdir}/qt6/plugins/konqueror_kcms
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_bookmarks.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_history.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_konq.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_performance.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_appearance.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_behavior.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_cache.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_cookies.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_filter.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_general.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_java_js.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_tabs.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_useragent.so
%{_libdir}/qt6/plugins/konqueror_kget_browser_integration.so
%{_libdir}/qt6/plugins/temporarysavedir.so
%{_libdir}/qt6/plugins/uachangerplugin.so
%{_libdir}/qt6/plugins/webarchiverplugin.so
%dir %{_libdir}/qt6/plugins/webenginepart
%dir %{_libdir}/qt6/plugins/webenginepart/kpartplugins
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/akregatorkonqfeediconwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/autorefreshwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/babelfishpluginwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/konqueror_kget_browser_integrationwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/uachangerpluginwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/temporarysavedirwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/webenginepart/kpartplugins/webarchiverpluginwebenginepart_kpartplugins.so
%{_libdir}/qt6/plugins/kf6/thumbcreator/webarchivethumbnail.so
%{_libdir}/libKF6KonqSettings.so.*.*
%ghost %{_libdir}/libKF6KonqSettings.so.?

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/akregator
%dir %{_datadir}/akregator/pics
%{_datadir}/akregator/pics/feed.png
%{_desktopdir}/bookmarks.desktop
%{_desktopdir}/kcm_bookmarks.desktop
%{_desktopdir}/kfmclient.desktop
%{_desktopdir}/kfmclient_dir.desktop
%{_desktopdir}/kfmclient_html.desktop
%{_desktopdir}/kfmclient_war.desktop
%{_desktopdir}/konqbrowser.desktop
%{_desktopdir}/org.kde.konqueror.desktop
%{_datadir}/config.kcfg/kcreatewebarchive.kcfg
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.Main.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.MainWindow.xml
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/actions/*.png
%dir %{_datadir}/kcmcss
%{_datadir}/kcmcss/template.css
%{_datadir}/kconf_update/webenginepart.upd
%dir %{_datadir}/kcontrol
%dir %{_datadir}/kcontrol/pics
%{_datadir}/kcontrol/pics/onlyone.png
%{_datadir}/kcontrol/pics/overlapping.png
%dir %{_datadir}/kf6/kbookmark
%{_datadir}/kf6/kbookmark/directory_bookmarkbar.desktop
%dir %{_datadir}/kio_bookmarks
%{_datadir}/kio_bookmarks/kio_bookmarks.css
%{_datadir}/konqsidebartng
%{_datadir}/konqueror
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%{_datadir}/qlogging-categories6/akregatorplugin.categories
%{_datadir}/qlogging-categories6/fsview.categories
%{_datadir}/qlogging-categories6/konqueror.categories
%dir %{_datadir}/webenginepart
%{_datadir}/webenginepart/error.html

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/konq_events.h
%{_includedir}/KF6/konq_historyentry.h
%{_includedir}/KF6/konq_historyprovider.h
%{_includedir}/KF6/konq_kpart_plugin.h
%{_includedir}/KF6/konq_popupmenu.h
%{_includedir}/KF6/konq_version.h
%{_includedir}/KF6/konqsidebarplugin.h
%{_includedir}/KF6/libkonq_export.h
%{_includedir}/KF6/konqsettings.h
%{_includedir}/KF6/konqsettings_version.h
%{_includedir}/KF6/libkonqsettings_export.h
%{_includedir}/KF6/selectorinterface.h
%{_libdir}/cmake/KF6Konq
%{_libdir}/libKF6Konq.so
%{_libdir}/libkonqsidebarplugin.so
%{_libdir}/libkwebenginepart.so
%{_libdir}/libKF6KonqSettings.so
